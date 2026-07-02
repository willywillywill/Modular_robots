#!/usr/bin/env python3
#coding=utf-8

import time
import rospy
from Rosmaster_Lib import Rosmaster
from ipywidgets import interact
import ipywidgets as widgets
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import tf
import serial
import math


bot = Rosmaster(com="/dev/ttyUSB0")
bot.create_receive_threading()
while 1:
    try:
        imu_attitude_data = bot.get_imu_attitude_data(ToAngle=True)
        print(imu_attitude_data)
    except rospy.ROSInterruptException:
        break
del bot