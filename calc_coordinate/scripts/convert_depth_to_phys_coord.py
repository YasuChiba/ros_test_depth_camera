#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pyrealsense2

def convert_depth_to_phys_coord(x,z,X0,Y0,Z0,theta0_x,theta0_z,d, horizontal_FOV, vertical_FOV):
    d_theta_x =  horizontal_FOV/360.0*math.pi*2 #カメラ画角（水平方向）
    d_theta_z = vertical_FOV/360.0*math.pi*2 #カメラ画角（垂直方向）
    Lx = 640.0 #画像幅
    Lz = 480.0 #画像高さ

    # 水平方向
    atan_y = 1
    atan_x = (2*x-Lx)/Lx*math.tan(d_theta_x/2)
    theta_dash_x = math.atan2(atan_y,atan_x)
    theta_x = theta0_x - theta_dash_x
    X = X0 + d*math.cos(theta_x)
    Y = Y0 + d*math.sin(theta_x)
    # 垂直方向
    atan_y = 1
    atan_z = (2*z-Lz)/Lz*math.tan(d_theta_z/2)
    theta_dash_z = math.atan2(atan_y,atan_z)
    theta_z = theta0_z - theta_dash_z
    Z = Z0 + d*math.sin(theta_z)
    return X, Y, Z

#x→右方向  y→下方向　のピクセル int
#depth (meter)   float
#cameraInfo: sensor_msgs/CameraInfo
def convert_depth_to_phys_coord_using_realsense(x, y, depth, cameraInfo):

  _intrinsics = pyrealsense2.intrinsics()
  _intrinsics.width = cameraInfo.width
  _intrinsics.height = cameraInfo.height
  _intrinsics.ppx = cameraInfo.K[2]
  _intrinsics.ppy = cameraInfo.K[5]
  _intrinsics.fx = cameraInfo.K[0]
  _intrinsics.fy = cameraInfo.K[4]
  #_intrinsics.model = cameraInfo.distortion_model
  _intrinsics.model  = pyrealsense2.distortion.none 	

  _intrinsics.coeffs = [i for i in cameraInfo.D]

  result = pyrealsense2.rs2_deproject_pixel_to_point(_intrinsics, [x, y], depth)
  #print(result)

  #result[0]: right
  #result[1]: down
  #result[2]: forward
  return result[2], -result[0], -result[1]

