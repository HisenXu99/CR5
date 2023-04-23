#! /usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
import random

#图片话题相关
import numpy as np 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError 
import cv2
import time

cam0_path  = '/home/hisen/Project/Data/CR5_picture/' 

def callback(data,x,y,bridge):
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
    x=random.uniform(-1,1)         
    y=random.uniform(0.2,1)
    image_name=str(round(x,3))+"&"+str(round(y,3))+ ".jpg" 
    cv2.imwrite(cam0_path + image_name, cv_img)
    pose_publisher(self.x,self.y)
    #cv2.imshow("image_name" , cv_img)
    #cv2.waitKey(3)


def pose_publisher():
    bridge = CvBridge()
    pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
    pose_msg = ModelState()
    pose_msg.model_name = 'beer'
    x=random.uniform(-1,1)         
    y=random.uniform(0.2,1)
    rate = rospy.Rate(1)
    pose_msg.pose.position.x = x
    pose_msg.pose.position.y = y
    pose_msg.pose.position.z = 0.965
    pub.publish(pose_msg)
    rospy.Subscriber('/camera/image_raw', Image, callback(Image,x,y,bridge),queue_size=1)
    rate.sleep()


class pose_publisher():
    def __init__(self) -> None:
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
        self.pose_msg = ModelState()
        self.pose_msg.model_name = 'beer'
        self.x=1.0       
        self.y=1.0
        self.pose()


    def pose(self):
        rate = rospy.Rate(1)
        self.x=random.uniform(-1,1)         
        self.y=random.uniform(0.2,1)
        self.pose_msg.pose.position.x = self.x
        self.pose_msg.pose.position.y = self.y
        self.pose_msg.pose.position.z = 0.965
        self.pub.publish(self.pose_msg)
        rospy.Subscriber('/camera/image_raw', Image, self.callback,queue_size=1)
        rate.sleep()

    def callback(self,data):
        cv_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
        x=random.uniform(-1,1)         
        y=random.uniform(0.2,1)
        image_name=str(round(x,3))+"&"+str(round(y,3))+ ".jpg" 
        cv2.imwrite(cam0_path + image_name, cv_img)
        #cv2.imshow("image_name" , cv_im


if __name__ == '__main__':
    node=rospy.init_node('GetPicture_changepose')
    pose_publisher()
    rospy.spin()