#!/usr/bin/env python
# coding=UTF-8
'''
此程序为测试测试程序， 用以测试message_filters同时
订阅两个topic，可以同时进行数据处理。
'''
import rospy, math, random, cv_bridge, cv2
import message_filters
from cv_bridge import CvBridge,CvBridgeError
from sensor_msgs.msg import Image, CameraInfo
from gazebo_msgs.msg import ModelState

cam0_path  = '/home/hisen/Project/Data/CR5_picture/'    # 已经建立好的存储cam0 文件的目录


def multi_callback(Subcriber_camera, Subcriber_pose):
    bridge = cv_bridge.CvBridge()
    #pose_msg = ModelState()
    array=[0.0,0.0]
    cv_img = bridge.imgmsg_to_cv2(Subcriber_camera, 'bgr8')#常规操作
    array[0] = round(Subcriber_pose.pose.position.x,3)
    array[1] = round(Subcriber_pose.pose.position.y,3)
    image_name=str(array[0])+"&"+str(array[1])+ ".jpg" 
    print(image_name)
    cv2.imwrite(cam0_path + image_name, cv_img)
    
    # cv2.imshow("window", color)
    # cv2.imshow("window2", depth)
    # cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node('get_picture', anonymous=True)#初始化节点

    #这种情况图片总是滞后于位置一张，应该是gazebo的更新比较慢。所以获取的图片还是没发生变化的。
    subcriber_pose = message_filters.Subscriber('gazebo/set_model_state', ModelState)#订阅第二个话题，beer位置信息
    subcriber_camera = message_filters.Subscriber('/camera/image_raw', Image,queue_size=1)#订阅第一个话题，rgb图像
    
 
    sync = message_filters.ApproximateTimeSynchronizer([subcriber_camera, subcriber_pose], 10,1,allow_headerless=True)#同步时间戳，具体参数含义需要查看官方文档。
    sync.registerCallback(multi_callback)#执行反馈函数
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("over!")
        cv2.destroyAllWindows()

