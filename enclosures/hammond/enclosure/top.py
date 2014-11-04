from __future__ import print_function
import os
from py2gcode import cnc_boundary
from py2gcode import cnc_pocket
from py2gcode import gcode_cmd

visualize = False 
feedrate = 40.0
safeZ = 0.5
startZ = 0.0
if visualize:
    depth = 0.02 
    toolDiam = 0.001
else:
    depth = 0.15
    toolDiam = 0.125

maxCutDepth = 0.04
startDwell = 2.0

xBackoff = 2.0
yBackoff = 1.0
zBackoff = 1.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = { 
        'centerX'      : -0.8767,
        'centerY'      : 0.0,
        'width'        : 0.6061,
        'height'       : 2.13,
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
lcdBoundary = cnc_boundary.RectBoundaryXY(param)
prog.add(lcdBoundary)


param = { 
        'centerX'       : -1.61,
        'centerY'      : 0.0,
        'radius'       : 0.5*0.4,
        'depth'        : depth,
        'startZ'       : startZ,
        'safeZ'        : safeZ,
        'toolDiam'     : toolDiam,
        'toolOffset'   : 'inside',
        'direction'    : 'ccw',
        'maxCutDepth'  : maxCutDepth,
        'startDwell'   : startDwell,
        }
buttonBoundary = cnc_boundary.CircBoundaryXY(param)
prog.add(buttonBoundary)

param = {
        'centerX'       : -1.61,
        'centerY'       : 0.0,
        'width'         : 0.62,
        'height'        : 0.62,
        'depth'         : 0.080,
        'thickness'     : 0.25,
        'startZ'       : startZ,
        'safeZ'        : safeZ,
        'overlap'       : 0.5,
        'overlapFinish' : 0.5,
        'maxCutDepth'  : maxCutDepth,
        'toolDiam'     : toolDiam,
        'direction'    : 'ccw',
        'startDwell'   : startDwell,
        'cornerCut'    : False
        }

pocket = cnc_pocket.RectAnnulusPocketXY(param)
prog.add(pocket)

if not visualize:
    prog.add(gcode_cmd.RapidMotion(x=xBackoff,y=yBackoff,z=zBackoff))

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
