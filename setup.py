from setuptools import setup
import os
from glob import glob

package_name = 'mech4640_tools'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jasper Grant',
    maintainer_email='jasper.grant@dal.ca',
    description='A ROS2 package to be used to hold scripts used in the mech4640 robotics class',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'lidar_pose_logger = mech4640_tools.lidar_pose_logger:main',
        ],
},
)
