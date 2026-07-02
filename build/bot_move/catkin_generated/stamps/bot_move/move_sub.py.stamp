#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import tf
import math
import time
from Rosmaster_Lib import Rosmaster 
from geometry_msgs.msg import Twist


class Driver:
    def __init__(self, bot):
        self.bot = bot

        rospy.init_node("driver_node")
        rospy.Subscriber("/move_topic", Twist, self.callback)
        rospy.spin()

    def callback(self, msg):
        vx = msg.linear.x
        vz = msg.angular.z
        rospy.loginfo("driver_node-> vx: %f, vz: %f", vx, vz)
        self.bot.set_car_motion(vx, 0, vz)


if __name__ == "__main__":
    try:
        com_port = rospy.get_param("~com_port", "/dev/ttyUSB0")
        bot = Rosmaster(com=com_port)
        driver = Driver(bot)

    except rospy.ROSInterruptException:
        del bot