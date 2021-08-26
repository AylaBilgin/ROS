#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Subscriber
"""

"""
import rospy
from gorev.msg import HizMesafe

def hiz_fonksiyonu(mesaj):
    rospy.loginfo("Robot hizi: %s"%mesaj.hiz)

def mesajDinle():
    rospy.init_node("abone")
    rospy.Subscriber("maksimum_hiz",HizMesafe,hiz_fonksiyonu)
    rospy.spin()
    
mesajDinle()
"""

"""
import rospy
from gorev.msg import HizMesafe

def hiz_fonksiyonu(mesaj):
    rospy.loginfo("Robot hizi: %s"%mesaj.hiz)

def mesajDinle():
    rospy.init_node("abone")
    rospy.Subscriber("cmd_vel",HizMesafe,hiz_fonksiyonu)
    rospy.spin()
    
mesajDinle()
"""

"""

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from gorev.msg import HizMesafe

class GorevBit():
    def __init__(self):
        rospy.init_node("mesafe_git")
        self.hedef = 1.0
        self.guncel = 0.0
        self.kontrol = True
        rospy.Subscriber("odom",Odometry,self.odomCallback)
        rospy.Subscriber("mesafe",HizMesafe,self.mesafeHızCallback)
        pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        hiz = Twist()
        self.max_hiz = 0.1
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.kontrol:
                hiz.linear.x = 0.05
                pub.publish(hiz)
                while self.max_hiz > hiz.linear.x:
                    hiz.linear.x = hiz.linear.x + 0.01
                    print(hiz.linear.x)
                    pub.publish(hiz)
                self.max_hiz = hiz.linear.x
                pub.publish(hiz)
            else:
                hiz.linear.x = 0.0
                pub.publish(hiz)
                rospy.loginfo("Hedefe varildi !")
                rospy.loginfo('Guncel hiz = {} Mesafe = {}'.format(self.max_hiz,self.guncel))
            rate.sleep()
    
    def odomCallback(self,mesaj):
        self.guncel = mesaj.pose.pose.position.x
        if self.guncel <= self.hedef:
            self.kontrol = True
        else:
            self.kontrol = False
            
    def mesafeHızCallback(self,mesaj):
        self.hedef = mesaj.x
        self.max_hiz = mesaj.v

try:
    GorevBit()
except rospy.ROSInterruptException:
    print("Dugum sonlandi !!!")


"""

import rospy
from gorev.msg import HizMesafe
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

class GorevBit():
    def __init__(self):
        rospy.init_node("abone")
        rospy.Subscriber("HizMesafe",HizMesafe,self.mesafeHızCallback)
        rospy.spin()
        
    def mesafeHızCallback(self,mesaj):
        self.hedef = mesaj.x
        self.max_hiz = mesaj.v
        self.kontrol = True
        pub = rospy.Publisher("cmd_vel",Twist,queue_size = 10)
        hiz = Twist()
        rate = rospy.Rate(10)
        hiz.linear.x = 0.05
        pub.publish(hiz)
        while not rospy.is_shutdown():
            rospy.Subscriber("odom",Odometry,self.odomCallback)
            if self.kontrol:  
                if mesaj.v > hiz.linear.x:
                    
                    hiz.linear.x = hiz.linear.x + 0.01
                    print(hiz.linear.x)
                    pub.publish(hiz)
                else:
                    hiz.linear.x = mesaj.v
                    pub.publish(hiz)
            else:
                hiz.linear.x = 0.0
                pub.publish(hiz)
                rospy.loginfo("Hedefe varildi !")
                
            rospy.loginfo('Guncel hiz = {} Mesafe = {}'.format(self.max_hiz,self.guncel))
            rate.sleep()
    
    def odomCallback(self,mesaj):
        self.guncel = mesaj.pose.pose.position.x
        if self.guncel <= self.hedef:
            self.kontrol = True
        else:
            self.kontrol = False
            
try:
    GorevBit()
except rospy.ROSInterruptException:
    print("Dugum sonlandi !!!")

