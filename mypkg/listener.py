#!/usr/bin/python3
# SPDX-FilecopyrightText: 2025 Makusa Ushu 
# SPDX-License-Identifer: BSD-3-Clause 

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import math

rclpy.init()
node =Node("listener")


def cb(msg):
    global node
    n = msg.data
    a = 1

    area = ( ( 1 / 2 ) * a * a * math.sin( ( 2 * math.pi ) / n ) * n )
    node.get_logger().info(f"角の数{n} 面積 {area}")


def main():
    pub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)


