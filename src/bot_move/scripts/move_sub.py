#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from Rosmaster_Lib import Rosmaster


class Driver:
    def __init__(self, bot):

        self.bot = bot

        self.max_vx = rospy.get_param("~max_vx", 0.3)
        self.max_wz = rospy.get_param("~max_wz", 1.0)

        rospy.Subscriber("/move_topic", Twist, self.cmd_callback)

        rospy.loginfo("driver_node -> start")
        rospy.loginfo("driver_node -> com_port: %s", com_port)

    def clamp(self, value, min_value, max_value):
        return max(min(value, max_value), min_value)

    def cmd_callback(self, msg):
        # 正常 move_base 應該輸出 linear.x
        vx = msg.linear.x

        # 暫時兼容：如果 planner 發到 linear.y，就拿 linear.y 當前進速度
        if abs(vx) < 0.001 and abs(msg.linear.y) > 0.001:
            vx = msg.linear.y

        wz = msg.angular.z

        # 限制速度，避免一開始太快
        vx = self.clamp(vx, -self.max_vx, self.max_vx)
        wz = self.clamp(wz, -self.max_wz, self.max_wz)

        rospy.loginfo_throttle(
            0.5,
            "driver_node -> vx: %.3f, wz: %.3f, raw_x: %.3f, raw_y: %.3f",
            vx, wz, msg.linear.x, msg.linear.y
        )

        # Rosmaster 控制
        # 阿克曼車通常不用 y，所以第二個參數給 0
        self.bot.set_car_motion(vx, 0.0, wz)


if __name__ == "__main__":
    rospy.init_node("move_subscriber")

    try:
        com_port = rospy.get_param("~com_port", "/dev/ttyUSB1")
        bot = Rosmaster(com=com_port)
        driver = Driver(bot)
        rospy.spin()
    except rospy.ROSInterruptException:
        del bot
        