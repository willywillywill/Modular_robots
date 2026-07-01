#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import tf
import math
from Rosmaster_Lib import Rosmaster 
import time

class Odom:
    def __init__(self, bot):
        self.bot = bot

        rospy.init_node("odom_node")
        self.pub = rospy.Publisher("/odom", Odometry, queue_size=10)
        self.br = tf.TransformBroadcaster()
        self.x = 0.0
        self.y = 0.0

        self.last_time = time.time()


    def run(self):
        rate = rospy.Rate(50)
        rospy.loginfo("odom_node-> start publishing odom")
        try:
            while not rospy.is_shutdown():
                now = time.time()
                dt = now - self.last_time
                self.last_time = now
                # ===== 1. 讀 IMU =====
                roll, pitch, yaw = self.bot.get_imu_attitude_data(ToAngle=False)
                rospy.loginfo("odom_node-> roll: %f, pitch: %f, yaw: %f", roll, pitch, yaw)
                # ===== 2. 讀速度 =====
                vx, vy, vz = self.bot.get_motion_data()
                # ===== 3. 用 yaw 把車體速度轉世界座標 =====
                vx_world = vx * math.cos(yaw) - vy * math.sin(yaw)
                vy_world = vx * math.sin(yaw) + vy * math.cos(yaw)
                # ===== 4. 積分位置 =====
                self.x += vx_world * dt
                self.y += vy_world * dt
                # ===== 5. quaternion =====
                q = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
                # ===== 6. publish odom =====
                odom = Odometry()
                odom.header.stamp = rospy.Time.now()
                odom.header.frame_id = "odom"
                odom.child_frame_id = "base_link"
                odom.pose.pose.position.x = self.x
                odom.pose.pose.position.y = self.y
                odom.pose.pose.orientation = Quaternion(*q)
                odom.twist.twist.linear.x = vx
                odom.twist.twist.linear.y = vy
                odom.twist.twist.angular.z = vz
                self.pub.publish(odom)

                
                self.br.sendTransform((self.x, self.y, 0),
                                      q,
                                      rospy.Time.now(),
                                      "base_link",
                                      "odom")

                rate.sleep()
        except rospy.ROSInterruptException:
            rospy.loginfo("odom_node-> stop publishing odom")


if __name__ == "__main__":
    try:
        com_port = rospy.get_param("~com_port", "/dev/ttyUSB0")
        bot = Rosmaster(com=com_port)
        bot.create_receive_threading()
        odom = Odom(bot)
        odom.run()

    except rospy.ROSInterruptException:
        del bot