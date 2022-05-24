#!/usr/bin/env python3

import math
import rospy
from std_msgs.msg import Float32

def receive_degree(msg): # call back function
    # formula: (deg * pi) / 180
    rads = msg.data * math.pi / 180
    rospy.loginfo(f'{msg.data} -> {rads}')

if __name__ == '__main__':
    rospy.init_node('deg2rad') # recommended, same as filename
    pub = rospy.Subscriber('/degree_pub', Float32, receive_degree)
    rospy.spin() # without spin(), this subscriber node will be terminated & inactive!
