#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PointStamped, Twist, Vector3, Pose, Point, Quaternion
from gazebo_msgs.msg import ModelState

import numpy as np
import tf
import math





class ControlObject:

  def __init__(self):
    rospy.init_node('control_objec')
    self.pub_position_marker = rospy.Publisher("/gazebo/set_model_state", ModelState, queue_size=10)

    self.current_x = 0
    self.current_y = 0
    self.current_z = 1
  

    r = rospy.Rate(1)
    while not rospy.is_shutdown():
      self.do_something()
      r.sleep()
  

  def do_something(self):


    point = Point(self.current_x, self.current_y, self.current_z)
    orientation = Quaternion(0, 0, 0, 0)
    pose = Pose(point,orientation)
    ms = ModelState()
    ms.pose = pose
    ms.model_name = "obje_1"
    ms.reference_frame = "world"
    print(ms)

    self.pub_position_marker.publish(ms)

    self.current_x += 0.01
    self.current_y += 0.01
    self.current_z += 0






if __name__ == '__main__':
    try:
        ControlObject()
    except rospy.ROSInterruptException:
        pass

