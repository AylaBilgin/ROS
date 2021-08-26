#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Service
"""
"""
import rospy
from gorev.srv import Goruntu
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

def kameraFonksiyon(solust_x,solust_y,genislik,yukseklik):
    hiz = 0.5
    sure = istek.x 

def cevapGonder():
    rospy.init_node("server", anonymous = True)
    rospy.Service("kamera",Goruntu,kameraFonksiyon)
    rospy.spin()

cevapGonder()
"""

import rospy
from gorev.srv import GoruntuKirpma
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class RobotKamera():
    def __init__(self):
        rospy.init_node("server", anonymous = True)
        rospy.Service("kamera",GoruntuKirpma,self.kameraFonksiyon)
        rospy.Subscriber("camera/rgb/image_raw",Image,self.kameraCallback)
        self.bridge = CvBridge()
        rospy.spin()
        
    def kameraCallback(self,mesaj):
        img = self.bridge.imgmsg_to_cv2(mesaj,"bgr8")
        kirpilmis = img[self.a:self.a+self.c, self.b:self.b+self.d]
        cv2.imshow("Robot Kamerasi",img)
        cv2.imshow("Kirpilmis Goruntu",kirpilmis)
        cv2.waitKey(1)
        
    def kameraFonksiyon(self,koordinatlar):
        self.a = koordinatlar.x
        self.b = koordinatlar.y
        self.c = koordinatlar.w
        self.d = koordinatlar.h
        print("Goruntu kirpildi ! ") 
        

RobotKamera()
