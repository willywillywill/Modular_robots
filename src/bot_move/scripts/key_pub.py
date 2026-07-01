#!/usr/bin/env python3
#coding=utf-8

import rospy
from geometry_msgs.msg import Twist

def key_pub():
    pub = rospy.Publisher('/move_topic', Twist, queue_size=10)
    rospy.init_node('key_pub', anonymous=True)
    twist_msg = Twist()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist_msg.linear.x, twist_msg.angular.z = map(float, input("input： ").split())
        pub.publish(twist_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        key_pub()
    except rospy.ROSInterruptException:
        pass


"""


"""