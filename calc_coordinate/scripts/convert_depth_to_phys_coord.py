#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


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


def convert_depth_to_phys_coord_from_pointcloud(x, z, pcl):
  point_index = u * pcl.point_step + v * pcl.row_step
  point_idx_x = point_index + pcl.fields[0].offset
  point_idx_y = point_index + pcl.fields[1].offset
  point_idx_z = point_index + pcl.fields[2].offset

  x = pcl.data[point_idx_x]
  y = pcl.data[point_idx_y]
  z = pcl.data[point_idx_z]

  return x,y,z
  
