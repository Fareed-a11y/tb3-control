#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_rotate_node')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

rate = rospy.Rate(10)

move_cmd = Twist()
stop_cmd = Twist()
rotate_cmd = Twist()

move_cmd.linear.x = 0.2
rotate_cmd.angular.z = 0.5

# Move forward
start = rospy.Time.now()

while rospy.Time.now() - start < rospy.Duration(3):
    pub.publish(move_cmd)
    rate.sleep()

# Stop
for i in range(10):
    pub.publish(stop_cmd)
    rate.sleep()

rospy.sleep(1)

# Rotate
start = rospy.Time.now()

while rospy.Time.now() - start < rospy.Duration(4):
    pub.publish(rotate_cmd)
    rate.sleep()

# Final stop
for i in range(10):
    pub.publish(stop_cmd)
    rate.sleep()
