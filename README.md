# mech4640 Tools

This repository contains ROS2 nodes required for the mech4640 course at Dalhousie University.

## Tools

### Lidar Pose Logger
This node logs [LaserScan](https://docs.ros.org/en/lunar/api/sensor_msgs/html/msg/LaserScan.html) messages from the topic `/scan` with the label 'LIDAR' and [Odometry](https://docs.ros.org/en/lunar/api/nav_msgs/html/msg/Odometry.html) messages from the topic `/odom` with the label 'ODOM'. The logged data is saved to the log 'lidar_pose_log.txt' (home directory) in the format:

```
LIDAR,<LaserScan message data>
ODOM,<Odometry message data>
```

To launch node use the command:
```bash
ros2 run mech4640_tools lidar_pose_logger
````
