#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('tb3_keyboard_control')

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

move = Twist()

print("""
Commands:
---------
move      -> forward
back      -> backward
left      -> rotate left
right     -> rotate right
stop      -> stop robot
exit      -> quit
""")

while not rospy.is_shutdown():

    cmd = input("Enter command: ")

    move = Twist()

    if cmd == "move":
        move.linear.x = 0.2

    elif cmd == "back":
        move.linear.x = -0.2

    elif cmd == "left":
        move.angular.z = 0.5

    elif cmd == "right":
        move.angular.z = -0.5

    elif cmd == "stop":
        pass

    elif cmd == "exit":
        pub.publish(Twist())
        break

    else:
        print("Unknown command")
        continue

    pub.publish(move)
