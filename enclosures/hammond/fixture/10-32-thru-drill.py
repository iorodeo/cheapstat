from __future__ import print_function
import os
from py2gcode import gcode_cmd
from py2gcode import cnc_drill


safeZ = 0.15
stepZ = 0.05
startZ = 0.0
stopZ = -0.3 
feedrate = 4.0
startDwell = 2.0

posList = [(-1.75, 0.0),(1.75,0)]  

prog = gcode_cmd.GCodeProg()
prog.add(gcode_cmd.GenericStart())
prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.FeedRate(feedrate))

for xPos, yPos in posList: 
    drillDict =  { 
            'centerX'    : xPos,
            'centerY'    : yPos,
            'startZ'     : startZ,
            'stopZ'      : stopZ,
            'safeZ'      : safeZ,
            'stepZ'      : stepZ,
            'startDwell' : startDwell, 
            }
    drill = cnc_drill.PeckDrill(drillDict)
    prog.add(drill)
    prog.add(gcode_cmd.Space())

prog.add(gcode_cmd.Space())
prog.add(gcode_cmd.End(),comment=True)
print(prog)
baseName, dummy = os.path.splitext(__file__)
fileName = '{0}.ngc'.format(baseName)
print(fileName)
prog.write(fileName)
