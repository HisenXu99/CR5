#! /usr/bin/env python
import rospy
from gazebo_msgs.msg import ModelState
import random

def pose_publish():
    # 改变模型pose
    pose_pub = rospy.Publisher('gazebo/set_model_state', ModelState, queue_size=10)
    pose_msg = ModelState()
    pose_msg.model_name = 'beer'
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        x=random.uniform(-1,1)
        y=random.uniform(0.2,1)
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = 0.965
        pose_pub.publish(pose_msg)
        rate.sleep()
        rate.sleep()
        rate.sleep()
        rate.sleep()
        rate.sleep()

def main():
    rospy.init_node('change_pose', anonymous=True)
    try:
        pose_publish()
    except rospy.ROSInterruptException:
        pass

if __name__ == '__main__':
    main()