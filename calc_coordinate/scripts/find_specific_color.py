#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import math


# 0 <= h <= 179 (色相)　OpenCVではmax=179なのでR:0(180),G:60,B:120となる
# 0 <= s <= 255 (彩度)　黒や白の値が抽出されるときはこの閾値を大きくする
# 0 <= v <= 255 (明度)　これが大きいと明るく，小さいと暗い
# ここでは青色を抽出するので120±20を閾値とした
LOW_COLOR = np.array([20, 80, 80])
HIGH_COLOR = np.array([60, 255, 255])
# 抽出する青色の塊のしきい値
AREA_RATIO_THRESHOLD = 0.00001
def find_specific_color(frame):
    """
    指定した範囲の色の物体の座標を取得する関数
    frame: 画像
    AREA_RATIO_THRESHOLD: area_ratio未満の塊は無視する
    LOW_COLOR: 抽出する色の下限(h,s,v)
    HIGH_COLOR: 抽出する色の上限(h,s,v)
    """

    # 高さ，幅，チャンネル数
    height,width,c = frame.shape

    # hsv色空間に変換
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    #cv2.imwrite('tmp2.png', hsv )

    # 色を抽出する
    ex_img = cv2.inRange(hsv,LOW_COLOR,HIGH_COLOR)
    #cv2.imwrite('tmp3.png', ex_img )

    # 輪郭抽出
    _,contours,hierarchy = cv2.findContours(ex_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    # 面積を計算
    areas = np.array(list(map(cv2.contourArea, contours)))
    #print(len(areas) )
    if len(areas) == 0 or np.max(areas) / (height*width) < AREA_RATIO_THRESHOLD:
        # 見つからなかったらNoneを返す
        #print("the area is too small")
        return None
    else:
        # 面積が最大の塊の重心を計算し返す
        max_idx = np.argmax(areas)
        max_area = areas[max_idx]
        result = cv2.moments(contours[max_idx])
        x = int(result["m10"]/result["m00"])
        y = int(result["m01"]/result["m00"])
        return (x, y)
        


