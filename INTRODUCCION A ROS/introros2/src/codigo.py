#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo("Valor recibido: %d", msg.data)

def main():
    # Inicializa el nodo
    rospy.init_node('mi_suscriptor')

    # Crea un suscriptor para el tema "valores_enteros"
    sub = rospy.Subscriber('valores_enteros', Int32, callback)

    # Espera hasta que se cierre el nodo
    rospy.spin()

if __name__ == '__main__':
    main()
