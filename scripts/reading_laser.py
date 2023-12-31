#! /usr/bin/env python3

import rclpy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):
  # 120 degrees into 3 regions
  # receive a value of range between 0 and 10.
  regions = [ 
    min(min(msg.ranges[0:2]), 10),
    min(min(msg.ranges[3:5]), 10),
    min( min(msg.ranges[6:9]), 10),
    ]

  rclpy.loginfo(regions)

def main():
  rclpy.init_node('reading_laser')
  sub= rclpy.Subscriber("/robot/laser/scan", LaserScan, callback_laser)

  rclpy.spin()

if __name__ == '__main__':
  main()