#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import PointStamped, Twist, Vector3, Pose, Point, Quaternion
from gazebo_msgs.msg import ModelState, ModelStates

import numpy as np
import tf
import math





class ControlObject:

  def __init__(self):
    rospy.init_node('control_objec')
    rospy.Subscriber("/gazebo/model_states", ModelStates, self.model_states_listener)

    self.pub_position_marker = rospy.Publisher("/gazebo/set_model_state", ModelState, queue_size=10)

    self.currentPoint = Point(8,-5,1)
  
    while not rospy.is_shutdown():
      direction = raw_input('w: forward, s: backward, a: left, d: right > ')
      if 'w' in direction:
          self.currentPoint.z += 0.1
      if 's' in direction:
          self.currentPoint.z -= 0.1
      if 'a' in direction:
          self.currentPoint.x -= 0.1
      if 'd' in direction:
          self.currentPoint.x += 0.1
      if 'r' in direction:
          self.currentPoint.y += 0.1
      if 'f' in direction:
          self.currentPoint.y -= 0.1
      if 'q' in direction:
          break

      self.do_something()
  

  def do_something(self):


    point = self.currentPoint
    orientation = Quaternion(0, 0, 0, 0)
    pose = Pose(point,orientation)
    ms = ModelState()
    ms.pose = pose
    ms.model_name = "obje_1"
    ms.reference_frame = "world"
    print(ms)

    self.pub_position_marker.publish(ms)


  def model_states_listener(self, data):
    index = data.name.index("obje_1")

    pose = data.pose[index]

    self.currentPoint = pose.position

  



if __name__ == '__main__':
    try:
        ControlObject()
    except rospy.ROSInterruptException:
        pass

