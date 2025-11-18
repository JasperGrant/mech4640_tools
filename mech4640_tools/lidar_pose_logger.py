#! /usr/bin/env python3
# Script to start a subscriber which logs messages from LIDAR and Odometry topics
# Written by Jasper Grant
# 2025-11-18

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
import logging

# Configure logging
logging.basicConfig(
    filename='lidar_pose_log.txt',
    level=logging.INFO,
    format='%(message)s'
)

class LidarPoseLogger(Node):

    def __init__(self):
        super().__init__('logger_node')

        self.lidar_subscription = self.create_subscription(
            LaserScan,
            'scan',
            self.lidarCallback,
            qos_profile=QoSProfile(
                reliability=ReliabilityPolicy.BEST_EFFORT,
                history=HistoryPolicy.KEEP_LAST,
                depth=5
            )
        )
        self.pose_subscription = self.create_subscription(
            Odometry,
            'odom',
            self.odomCallback,
            10
        )

    def lidarCallback(self, msg):
        logging.info(f"LIDAR,{msg}")

    def odomCallback(self, msg):
        logging.info(f"ODOM,{msg}")
        pass

def main():

    rclpy.init()

    lidar_pose_logger = LidarPoseLogger()

    rclpy.spin(lidar_pose_logger)

    lidar_pose_logger.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()