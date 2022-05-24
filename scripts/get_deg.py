#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def talker():
    pub = rospy.Publisher('/degree_pub', Float32, queue_size=10)
    rospy.init_node('get_deg', anonymous=True)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = Float32()
        msg.data = rospy.get_param('/degree')
        pub.publish(msg)
        rate.sleep()
    rospy.loginfo('Node stopped')

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
