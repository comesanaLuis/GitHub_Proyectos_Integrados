#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

range_ahead=10
range_left=10
range_right=10

def scan_callback(msg):
    global range_ahead, range_left, range_right

    range_ahead=msg.ranges[len(msg.ranges)/2]
    range_left=msg.ranges[len(msg.ranges)/10]
    range_right=msg.ranges[(len(msg.ranges)*9)/10]

def scan_and_move():
    rospy.init_node ('movedor_robot')
    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)
    scan_sub=rospy.Subscriber('/kobuki/laser/scan',LaserScan,scan_callback)
    rate=rospy.Rate(4)
    move=Twist()
    turn=0.0

    while not rospy.is_shutdown():
        
        if (range_ahead>1): #adelante libre
           move.linear.x=1
           move.angular.z=0.0
        else:
           move.linear.x=0.0
           if (range_left>range_right): # girar a la derecha
              turn=-1.35
           else: # girar a la izquierda
              turn=1.35
           move.angular.z=turn

        pub.publish(move)

        rate.sleep()

if __name__ == '__main__':
    try:
        scan_and_move()
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated. ")
