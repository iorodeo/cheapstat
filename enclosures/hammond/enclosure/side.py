from __future__ import print_function
import os
from py2gcode import cnc_boundary
from py2gcode import gcode_cmd

# -----------------------------------------------------------------------------
# Notes, 
# 
#  zero x at top of enclosure
#  zero y at seam between two halves 
#  hold in vise
# ------------------------------------------------------------------------------

feedrate = 22.0
safeZ = 0.25
startZ = 0.0
depth = 0.16
toolDiam = 0.125
#depth = 0.02 
#toolDiam = 0.001
maxCutDepth = 0.02
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = { 
        'centerX'      : 1.9654,
        'centerY'      : 0.2965,
        'width'        : 0.5,
        'height'       : 0.4,
        'depth'        : depth,
        'radius'       : 0.0,
        'startZ'       : startZ,
        'safeZ'        : safeZ,
        'toolDiam'     : toolDiam,
        'toolOffset'   : 'inside',
        'direction'    : 'ccw',
        'maxCutDepth'  : maxCutDepth,
        'startDwell'   : startDwell,
        
        }
usbBoundary = cnc_boundary.RectBoundaryXY(param)
prog.add(usbBoundary)


param = {
        'centerX'       : 3.4387,
        'centerY'       : 0.0,
        'width'         : 0.3,
        'height'        : 0.125,
        'depth'         : depth,
        'radius'       : 0.0,
        'startZ'       : startZ,
        'safeZ'        : safeZ,
        'toolDiam'     : toolDiam,
        'toolOffset'   : 'inside',
        'direction'    : 'ccw',
        'maxCutDepth'  : maxCutDepth,
        'startDwell'   : startDwell,
        }

wireBoundary= cnc_boundary.RectBoundaryXY(param)
prog.add(wireBoundary)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
