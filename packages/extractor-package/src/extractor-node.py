#!/usr/bin/env python

import rospy
import picamera
import picamera.array
from time import sleep
import os
import numpy as np
import cv2
import rosbag
from cv_bridge import CvBridge

from sensor_msgs.msg import CompressedImage

carName = os.environ['VEHICLE_NAME']
topicString = '/' + carName + '/camera_node/image/compressed'

pub = rospy.Publisher(topicString, CompressedImage, queue_size=10)

rospy.init_node('Image_Publisher')
rate = rospy.Rate(10)


bridge = CvBridge()
print('bridge')
with picamera.PiCamera() as camera:
  camera.resolution = (320, 240)

  while True:
      with picamera.array.PiRGBArray(camera) as output:
	  camera.capture(output, 'rgb')
	  output = output.array

	  image_message = bridge.cv2_to_compressed_imgmsg(output)

	  message = image_message
	  rospy.loginfo("Publishing image")
	  pub.publish(message)
	  rate.sleep()
