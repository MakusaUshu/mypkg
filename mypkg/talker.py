#!/usr/bin/python3
# SPDX-FilecopyrightText: 2025 Makusa Ushu
# SPDX-License-Identifer: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16MultiArray
import threading

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16MultiArray, "countup", 10)

n = 3
user_value = 1  

def input_thread():
    global user_value, n
    while True:
        try:
            user_value = int(input(""))
            n = 3
        except Exception:
            pass   

def cb():
    global n, user_value
    msg = Int16MultiArray()
    msg.data = [n, user_value]
    pub.publish(msg)
    n += 1

def main():
    t = threading.Thread(target=input_thread, daemon=True)
    t.start()

    node.create_timer(0.5, cb)
    rclpy.spin(node)

if __name__ == "__main__":
    main()
