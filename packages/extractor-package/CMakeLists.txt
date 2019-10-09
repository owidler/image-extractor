cmake_minimum_required(VERSION 2.8.3)
project(extractor-package)

find_package(catkin REQUIRED COMPONENTS
  rospy rosbag
)

catkin_package()
