#!/usr/bin/env python

import rospy, tf
from gazebo_msgs.srv import DeleteModel, SpawnModel
from geometry_msgs.msg import *

if __name__ == '__main__':
    print("Waiting for gazebo services...")
    rospy.init_node("spawn_products_in_bins")
    #rospy.wait_for_service("gazebo/delete_model")
    rospy.wait_for_service("gazebo/spawn_sdf_model")
    print("Got it.")
    delete_model = rospy.ServiceProxy("gazebo/delete_model", DeleteModel)
    spawn_model = rospy.ServiceProxy("gazebo/spawn_sdf_model", SpawnModel)

    with open("/root/catkin_ws/src/spawn_moving_object_in_gazebo/models/box1/model.sdf", "r") as f:
        product_xml = f.read()


    item_name   =   "obje_1"
    delete_model(item_name)
    print("Spawning model:%s", item_name)
    orient = Quaternion(0,0,0,0)
    #item_pose = Pose(Point(x=8, y=-5, z=1), orient)
    item_pose   =   Pose(Point(x=1, y=0,    z=1),   orient)

    spawn_model(item_name, product_xml, "", item_pose, "world")



    with open("/root/catkin_ws/src/spawn_moving_object_in_gazebo/models/box2/model.sdf", "r") as f:
        product_xml = f.read()


    item_name = "obje_2"
    delete_model(item_name)
    #print("Spawning model:%s", item_name)
    #orient = Quaternion(0,0,0,0)
    #item_pose   =   Pose(Point(x=8, y=-5,    z=1),   orient)
    #item_pose   =   Pose(Point(x=1, y=0,    z=1),   orient)
    #spawn_model(item_name, product_xml, "", item_pose, "world")
