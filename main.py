# !/usr/bin/env python
import rospy
from std_msgs.msg import String, Int8, Float64
from robot.robot import ExoRobot

r = ExoRobot()
def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %f', data.data)
    goal_angle = data.data
    r.step(goal_angle)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Float64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
