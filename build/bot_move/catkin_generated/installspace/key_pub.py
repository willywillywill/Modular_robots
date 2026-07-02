#!/usr/bin/env python3
#coding=utf-8

import rospy
from geometry_msgs.msg import Twist
import sys, select, termios, tty

tty.setraw(sys.stdin.fileno())
key = sys.stdin.read(1)
print(key)

"""
if __name__ == '__main__':

    pub = rospy.Publisher('/move_topic', Twist, queue_size=10)
    rospy.init_node('key_pub', anonymous=True)
    twist_msg = Twist()
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        if keyboard.press_and_release('w'):
            rospy.loginfo("key_pub-> w pressed")
        elif keyboard.press_and_release('s'):
            rospy.loginfo("key_pub-> s pressed")
            break
"""
