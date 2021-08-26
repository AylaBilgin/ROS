#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Publisher
"""
"""
import rospy
from gorev.msg import HizMesafe

def mesajYayinla():
    rospy.init_node("yayinci",anonymous=True)
    pub = rospy.Publisher("maksimum_hiz",HizMesafe,queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        max_hiz = "0.05"
        mesafe = "0.01"
        rospy.loginfo('max_hiz={} mesafe={}'.format(max_hiz,mesafe))
        pub.publish(max_hiz,mesafe)
        rate.sleep()
        
mesajYayinla()
"""

"""
import rospy
from gorev.msg import HizMesafe
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def hareket():
    rospy.init_node("yayinci",anonymous=True)
    pub = rospy.Publisher("cmd_vel",Twist,queue_size=10)
    hiz = Twist()
    
    max_hiz = 1.0
    mesafe = 1.0
    hiz.linear.x = 0.05
    
    while not (yer_degistirme == mesafe):
        pub.publish(hiz)
        print(yer_degistirme)
        if (max_hiz > hiz.linear.x):
            hiz.linear.x = hiz.linear.x + 0.01
            pub.publish(hiz)
            print(hiz.linear.x)
        else:
            hiz.linear.x = max_hiz
            pub.publish(hiz)
            print(hiz.linear.x)
        
    hiz.linear.x = 0.0
    pub.publish(hiz)
    print("Hedefe varıldı.")
hareket()

"""
        
"""
    mesafe = 5
    max_hiz = 0.1
    yer_degistirme = 0
    t0 = rospy.Time.now().to_sec()
    while (max_hiz != hiz.linear.x):
        pub.publish(hiz)
        t1 = rospy.Time.now().to_sec()
        yer_degistirme = hiz.linear.x * (t1-t0)
        if(yer_degistirme == mesafe):
            hiz.linear.x = 0
        hiz.linear.x = hiz.linear.x + 0.01
    pub.publish(hiz)
    rospy.loginfo("Hedefe varildi !")  
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

def mesajYayinla():
    rospy.init_node("yayinci",anonymous=True)
    pub = rospy.Publisher("HizMesafe",HizMesafe,queue_size = 10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        max_hiz = 0.1
        guncel = 0.5
        rospy.loginfo('Guncel hiz = {} Mesafe = {}'.format(max_hiz,guncel))
        pub.publish(max_hiz,guncel)
        rate.sleep()
        
mesajYayinla()