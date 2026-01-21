#!/usr/bin/python3
# SPDX-FilecopyrightText: 2025 Makusa Ushu
# SPDX-License-Identifer: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray
import math

def cb(msg):
    n = msg.data[0]   
    a = msg.data[1]   

    if n < 3:
        return

    area = 0.5 * a * a * math.sin((2 * math.pi) / n) * n
    print(f"角の数 {n}  外接円の半径 {a}  面積 {area}")

def main():
    rclpy.init()
    node = Node("listener")

    node.create_subscription(
        Int16MultiArray,
        "countup",
        cb,
        10
    )

    rclpy.spin(node)

if __name__ == "__main__":
    main()

