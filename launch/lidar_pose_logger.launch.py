# Launch file to start the lidar pose logger
# Written by Jasper Grant
# 2025-11-18

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='mech4640_tools',
			executable='lidar_pose_logger',
			name='logger_node',
			output='screen'
        )
    ])