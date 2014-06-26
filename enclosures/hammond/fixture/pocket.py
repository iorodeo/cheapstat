from __future__ import print_function
import os
from py2gcode import cnc_boundary
from py2gcode import cnc_pocket
from py2gcode import gcode_cmd

feedrate = 22.0
safeZ = 0.15
startZ = 0.0
depth = 0.15
toolDiam = 0.25
maxCutDepth = 0.02
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))



param = {
        'centerX'       : 0.0,
        'centerY'       : 0.0,
        'width'         : 2.365,
        'height'        : 0.9,
        'depth'         : 0.0315,
        'startZ'       : startZ,
        'safeZ'        : safeZ,
        'overlap'       : 0.6,
        'overlapFinish' : 0.6,
        'maxCutDepth'  : maxCutDepth,
        'toolDiam'     : toolDiam,
        'direction'    : 'ccw',
        'startDwell'   : startDwell,
        'cornerCut'    : True 
        }

pocket = cnc_pocket.RectPocketXY(param)
prog.add(pocket)

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
