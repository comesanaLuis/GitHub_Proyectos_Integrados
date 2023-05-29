#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32

def main():
    # Inicializa el nodo
    rospy.init_node('mi_nodo')

    # Crea un publicador para el tema "valores_enteros"
    pub = rospy.Publisher('valores_enteros', Int32, queue_size=10)

    # Solicita al usuario que ingrese un valor entero y lo publica en el tema
    while not rospy.is_shutdown():
        valor = input("Ingrese un valor entero: ")
        pub.publish(Int32(int(valor)))

if __name__ == '__main__':
    main()
