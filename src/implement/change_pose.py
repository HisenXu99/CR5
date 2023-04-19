#! /usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
import random

#图片话题相关
import numpy as np 
from sensor_msgs.msg import Image 
from cv_bridge import CvBridge, CvBridgeError 
import cv2

 
# cam0_path  = '/home/hisen/Project/Data/CR5_picture/'    # 已经建立好的存储cam0 文件的目录
# #cam1_path  = '/home/hltt3838/my_c++/VINS_test/BUAA_robot/cam1/'
 
# def callback(data):
#     # define picture to_down' coefficient of ratio
#     scaling_factor = 0.5
#     global count,bridge
#     count = count + 1
#     if count == 1:
#         count = 0
#         cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#         timestr = "%.6f" %  data.header.stamp.to_sec()
#               #%.6f表示小数点后带有6位，可根据精确度需要修改；
#         image_name = timestr+ ".jpg" #图像命名：时间戳.jpg
#         cv2.imwrite(cam0_path + image_name, cv_img)  #保存；
#         #cv2.imshow("frame" , cv_img)
#         #cv2.waitKey(3)
#     else:
#         pass
 

# def pose_publisher():
#     pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
#     pose_msg = ModelState()
#     pose_msg.model_name = 'beer'
#     rate = rospy.Rate(1)
#     while not rospy.is_shutdown():
#            x=random.uniform(-1,1)
#            y=random.uniform(0.2,1)
#            pose_msg.pose.position.x = x
#            pose_msg.pose.position.y = y
#            pose_msg.pose.position.z = 0.965
#            pub.publish(pose_msg)
#            rate.sleep()

# if __name__ == '__main__':
#     global count,bridge     
#     count = 0     
#     bridge = CvBridge()
#     rospy.init_node('pose_publisher')
#     rospy.Subscriber('/camera/image_raw', Image, callback)
#     #rospy.init_node('webcam_display', anonymous=True)
#     try:
#         pose_publisher()
#     except rospy.ROSInterruptException:
#         pass


 
cam0_path  = '/home/hisen/Project/Data/CR5_picture/'    # 已经建立好的存储cam0 文件的目录
#cam1_path  = '/home/hltt3838/my_c++/VINS_test/BUAA_robot/cam1/'
 
def callback(data):
    # define picture to_down' coefficient of ratio
    scaling_factor = 0.5
    global count,bridge,x,y
    count = count + 1
    rate = rospy.Rate(1)
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
    image_name=str(round(x,3))+"&"+str(round(y,3))+ ".jpg" 
    print(image_name)
    cv2.imwrite(cam0_path + image_name, cv_img)  #保存；
    rate.sleep()
    x=random.uniform(-1,1)         
    y=random.uniform(0.2,1)
    pose_publisher()
    #rate.sleep()
 

def pose_publisher():
    pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
    pose_msg = ModelState()
    pose_msg.model_name = 'beer'
    global x,y
    # x=random.uniform(-1,1)
    # y=random.uniform(0.2,1)
    pose_msg.pose.position.x = x
    pose_msg.pose.position.y = y
    pose_msg.pose.position.z = 0.965
    pub.publish(pose_msg)

if __name__ == '__main__':
    global count,bridge,x,y    
    count = 0      
    bridge = CvBridge()
    x=1.0
    y=1.0
    rospy.init_node('pose_publisher')
    rospy.Subscriber('/camera/image_raw', Image, callback)
    rospy.spin()