#!/usr/bin/env python3
import serial
import time
import rospy
from serial_stm32.msg import Verter

serial_port = '/dev/ttyACM0'  # Adjust as needed
baud_rate = 115200
ser = serial.Serial(serial_port, baud_rate)

def verter_callback(msg):
    print(f"Received: x={msg.x}, y={msg.y}")
    ser.write(f"{msg.x},{msg.y}".encode())  # Send a test message to the serial port

def verter_subscriber():
    rospy.init_node('verter_subscriber', anonymous=True)
    rospy.Subscriber('verter_topic', Verter, verter_callback)
    rospy.spin()

if __name__ == '__main__':
    verter_subscriber()