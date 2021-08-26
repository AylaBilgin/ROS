#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Client
"""

import rospy
from gorev.srv import GoruntuKirpma

def istekteBulun(x,y,w,h):
    rospy.wait_for_service("kamera")
    
    try:
        servis = rospy.ServiceProxy("kamera",GoruntuKirpma)
        cevap = servis(x,y,w,h)
        return cevap.koordinat
    except rospy.ServiceException:
        print("Hata oluştu !!!")
        
x = int(input("x koordinatini giriniz: "))
y = int(input("y koordinatini giriniz: "))
w = int(input("w degerini giriniz: "))
h = int(input("h degerini giriniz: "))

t = istekteBulun(x,y,w,h)
