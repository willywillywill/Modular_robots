#!/usr/bin/env python3
import rospy
from serial_stm32.msg import Verter


def verter_publisher():
    pub = rospy.Publisher('/verter_topic', Verter, queue_size=10)
    rospy.init_node('verter_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Verter()
        msg.x, msg.y = map(int, input().split())
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        verter_publisher()
    except rospy.ROSInterruptException:
        pass

"""
import rospy
from serial_stm32.msg import verter

def verter_publisher():
    pub = rospy.Publisher('/verter_topic', verter, queue_size=10)
    rospy.init_node('verter_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = verter()
        msg.x = 1.0
        msg.y = 2.0
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        verter_publisher()
    except rospy.ROSInterruptException:
        pass
"""