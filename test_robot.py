from robot.robot import ExoRobot
import time

r = ExoRobot()
# r.executeDebuger()
l = [1.5,1.3,1.2,1.0,0.5,0.0]
for a in l:
    r.step(a)
    print("step",a)
    time.sleep(0.1)