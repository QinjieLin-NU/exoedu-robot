"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Device

import rospy
from std_msgs.msg import String, Int8, Float64

# create the Robot instance.
robot = Robot()

# print(dir(robot))
# print(robot.getName())

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
motor = robot.getDevice('motor_sensorAdapter')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + 'I heard %f', data.data)
    # goal_angle = (data.data / 180.0) *3.14
    # motor.setPosition(0.0)

# def listener():
    # rospy.init_node('listener', anonymous=True)
    # rospy.Subscriber('chatter', Float64, callback)
    # rospy.spin()

# print("start listener")

# listener()
rospy.init_node('listener', anonymous=True)
# print("after listener")
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Enter here functions to send actuator commands, like:
    goal_angle = 0.0
    try:
        x = rospy.wait_for_message("chatter",Float64,timeout=0.1)
        goal_angle = (x.data / 180.0) *3.14
    except rospy.ROSException as e:
        pass
    motor.setPosition(goal_angle)
    # print("test")
    pass

# Enter here exit cleanup code.

