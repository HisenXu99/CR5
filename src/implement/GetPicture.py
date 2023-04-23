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


 
cam0_path  = '/home/hisen/Project/Data/CR5_picture/'    # 已经建立好的存储cam0 文件的目录
#cam1_path  = '/home/hltt3838/my_c++/VINS_test/BUAA_robot/cam1/'
 
# def callback(data):
#     # define picture to_down' coefficient of ratio
#     scaling_factor = 0.5
#     global bridge,x,y
#     #rate = rospy.Rate(1)
#     cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#     image_name=str(round(x,3))+"&"+str(round(y,3))+ ".jpg" 
#     #print(image_name)
#     cv2.imwrite(cam0_path + image_name, cv_img)  
#     #cv2.imshow("image_name" , cv_img)
#     x=random.uniform(-1,1)         
#     y=random.uniform(0.2,1)
#     print(x,"   ",y)
#     pose_publisher()
#     #rate.sleep()
 

# def pose_publisher(x,y):
#     pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
#     pose_msg = ModelState()
#     pose_msg.model_name = 'beer'
#     pose_msg.pose.position.x = x
#     pose_msg.pose.position.y = y
#     pose_msg.pose.position.z = 0.965
#     pub.publish(pose_msg)

# def get_picture():
#     rospy.init_node('pose_publisher',anonymous=True)
#     rate = rospy.Rate(1)
    
#     rospy.spin()


class GetPictures():
    def __init__(self) -> None:
        self.bridge = CvBridge()
        self.node=rospy.init_node('GetPicture_changepose')
        self.rate = rospy.Rate(1)
        self.count=0
        self.x=1.0
        self.y=1.0
        self.pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=1)
        self.pose_msg = ModelState()
        self.pose_msg.model_name = 'beer'
        rospy.Subscriber('/camera/image_raw', Image, self.callback,queue_size=1)

    def callback(self,data):
        #scaling_factor = 0.5
        self.count=self.count+1
        if self.count==1:
            self.count=0
            cv_img = self.bridge.imgmsg_to_cv2(data, "bgr8")
            image_name=str(round(self.x,3))+"&"+str(round(self.y,3))+ ".jpg" 
            cv2.imwrite(cam0_path + image_name, cv_img)
            self.x=random.uniform(-1,1)         
            self.y=random.uniform(0.2,1)
            self.pose_publisher()
            #cv2.imshow("image_name" , cv_img)
            #cv2.waitKey(3)
            self.rate.sleep()
        else:
            pass
    def pose_publisher(self):
        self.pose_msg.pose.position.x = self.x
        self.pose_msg.pose.position.y = self.y
        self.pose_msg.pose.position.z = 0.965
        self.pub.publish(self.pose_msg)



if __name__ == '__main__':
    GetPictures()
    rospy.spin()