import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

rclpy.int()
node =Node("lostener")


def cd(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    pub = node.create_subscription(int16, "countup", cb, 10)
    rclpy.spin(node)
