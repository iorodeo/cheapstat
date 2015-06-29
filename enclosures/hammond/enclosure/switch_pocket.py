from __future__ import print_function
import os
from py2gcode import cnc_boundary
from py2gcode import cnc_pocket
from py2gcode import gcode_cmd

visualize = False 
feedrate = 40.0
safeZ = 0.15
startZ = 0.0
if visualize:
    depth = 0.02
    toolDiam = 0.001
else:
    depth = 0.08
    toolDiam = 0.125

maxCutDepth = 0.04
startDwell = 2.0

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))


param = {
        'centerX'       : 0.0,
        'centerY'       : -0.060,
        'width'         : 0.76,
        'height'        : 0.508,
        'depth'         : depth,
        'thickness'     : toolDiam,
        'startZ'        : startZ,
        'safeZ'         : safeZ,
        'overlap'       : 0.5,
        'overlapFinish' : 0.5,
        'maxCutDepth'   : maxCutDepth,
        'toolDiam'      : toolDiam,
        'direction'     : 'ccw',
        'startDwell'    : startDwell,
        'cornerCut'     : True
        }

pocket = cnc_pocket.RectAnnulusPocketXY(param)
prog.add(pocket)

prog.add(gcode_cmd.Space())

if not visualize:
    prog.add(gcode_cmd.RapidMotion(**{'x': 0.0, 'y': 1.5, 'z': 3.0}))

prog.add(gcode_cmd.Space())


prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
