#!/usr/bin/env python

import roslib; 
roslib.load_manifest('pr2_python')
import rospy

from pr2_python import gripper

if __name__=='__main__':
    rospy.init_node("test_gripper", anonymous=True)
    gr = gripper.Gripper('right_arm')

    # Open
    gr.open()
    rospy.sleep(2.0)
    
    # Close
    gr.close()
