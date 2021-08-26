#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 22:55:17 2021

@author: ayla
"""

import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2
import numpy as np
import random
import operator

koordinat = []
for i in range(0,5):
    x=int(random.random() * 5)
    y=int(random.random() * 5)
    koordinat.append((x,y))
print("Gidilecek koordinatlar:",koordinat)

def baslangic_popülasyonu(boyut,koordinat_sayisi):
    popülasyon = []
    for i in range(0,boyut):
        popülasyon.append(yeni_üye(koordinat_sayisi))
    return popülasyon

def pick_mate(N):
    i=random.randint(0,N)
    print(i)
    return i


def distance(i,j):
    return np.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2)


def popülasyon_skoru(popülasyon, koordinat_listesi):  
    skorlar = []
    for i in popülasyon:
        print(i)
        skorlar.append(uyumluluk(i, koordinat_listesi))
        #print([uyumluluk(i, the_map)])
    return skorlar


def uyumluluk(rota,koordinat_listesi):
    skor=0
    for i in range(1,len(rota)):
        k=int(rota[i-1])
        l=int(rota[i])
        skor = skor + distance(koordinat_listesi[k],koordinat_listesi[l])
    return skor


def yeni_üye(koordinat_sayisi):
    pop=set(np.arange(koordinat_sayisi,dtype=int))
    rota=list(random.sample(pop,koordinat_sayisi))
    return rota


def crossover(a,b):
    cocuk=[]
    cocuk_A=[]
    cocuk_B=[]
    gen_A=int(random.random()* len(a))
    gen_B=int(random.random()* len(a))
    
    gen_baslangic=min(gen_A,gen_B)
    gen_son=max(gen_A,gen_B)
    
    for i in range(gen_baslangic,gen_son):
        cocuk_A.append(a[i])
        
    cocuk_B=[item for item in a if item not in cocuk_A]
    cocuk=cocuk_A+cocuk_B
     
    return cocuk


def mutasyon(rota,olasılık):
    rota=np.array(rota)
    for degisim_p in range(len(rota)):
        if(random.random() < olasılık):
            swapedWith = np.random.randint(0,len(rota))
            temp1=rota[degisim_p]
            temp2=rota[swapedWith]
            rota[swapedWith]=temp1
            rota[degisim_p]=temp2
    return rota


def secilim(popRanked, elitUye):
    secilimSonuc=[]
    sonuc=[]
    for i in popRanked:
        sonuc.append(i[0])
    for i in range(0,elitUye):
        secilimSonuc.append(sonuc[i])
    return secilimSonuc


def oran(popülasyon,koordinat_listesi):
    uygunlukSonuc = {}
    for i in range(0,len(popülasyon)):
        uygunlukSonuc[i] = uyumluluk(popülasyon[i],koordinat_listesi)
    return sorted(uygunlukSonuc.items(), key = operator.itemgetter(1), reverse = False)


def cins(havuz):
    cocuklar=[]
    for i in range(len(havuz)-1):
            cocuklar.append(crossover(havuz[i],havuz[i+1]))
    return cocuklar


def mutasyonluPopülasyon(cocuklar,mutasyon_orani):
    yeni_jenerasyon=[]
    for i in cocuklar:
        mutasyonlu_cocuk=mutasyon(i,mutasyon_orani)
        yeni_jenerasyon.append(mutasyonlu_cocuk)
    return yeni_jenerasyon

def çiftHavuz(popülasyon, secilimSonuc):
    çiftHavuz = []
    for i in range(0, len(secilimSonuc)):
        index = secilimSonuc[i]
        çiftHavuz.append(popülasyon[index])
    return çiftHavuz

def yeni_jenerasyon(koordinat_listesi,akim_popülasyon,mutasyon_orani,elit_üye):
    popülasyon_orani=oran(akim_popülasyon,koordinat_listesi)
    secilim_sonuc=secilim(popülasyon_orani,elit_üye)
    havuz=çiftHavuz(akim_popülasyon,secilim_sonuc)
    cocuklar=cins(havuz)  
    yeni_jenerasyon=mutasyonluPopülasyon(cocuklar,mutasyon_orani)
    return yeni_jenerasyon


def genetik_algoritma(koordinat_listesi,popülasyon_boyut=1000,elit_uye=75,mutasyon_orani=0.01,jenerasyon=2000):
    pop=[]
    gelisim = [] 
    koordinatSayisi=len(koordinat_listesi)
    popülasyon=baslangic_popülasyonu(popülasyon_boyut,koordinatSayisi)
    gelisim.append(oran(popülasyon,koordinat_listesi)[0][1])
    print(f"ilk rota mesafesi{gelisim[0]}")
    print(f"ilk rota {popülasyon[0]}")
    for i in range(0,jenerasyon):
        pop = yeni_jenerasyon(koordinat_listesi, popülasyon, mutasyon_orani, elit_uye)
        gelisim.append(oran(pop,koordinat_listesi)[0][1])
    
    rank_=oran(pop,koordinat_listesi)[0]
    print(f"En iyi rota :{pop[rank_[0]]} ")
    print(f"en iyi rota mesafesi {rank_[1]}")

    return rank_, pop

rank_,pop=genetik_algoritma(koordinat_listesi=koordinat)

#print(pop[rank_[0]])
array = []
array = pop[rank_[0]]
#print(array[1])
#print(koordinat[array[0]][1])
#hedef.x = koordinat[array[0]][0]
#hedef.y = koordinat[array[0]][1]
"""
class Tsp():
    def __init__(self):
        rospy.init_node("TSP")
        pub = rospy.Publisher("/cmd_vel",Twist,queue_size=1)
        self.x = 0.0
        self.y = 0.0
        self.theta = 0.0
        
        hedef = Point()
        hiz = Twist()
        rate = rospy.Rate(4)
        
        for i in range(len(koordinat)-1):
           hedef.y = koordinat[array[i]][0]
           hedef.x = koordinat[array[i]][1]
           print(hedef)
           
           while not (abs(hedef.x-x) < 0.01 and abs(hedef.y-y) < 0.01):
               rospy.Subscriber("/odom",Odometry,self.odomCallback)
               inc_x = hedef.x - self.x
               inc_y = hedef.y - self.y
               aci = atan2(inc_y,inc_x)
               
               if abs(aci - self.theta) > 0.1:
                   hiz = Twist()
                   hiz.linear.x = 0.0
                   hiz.angular.z = 0.3
                   pub.publish(hiz)
                 
               else:
                   hiz = Twist()
                   hiz.linear.x = 0.1
                   hiz.angular.z = 0.0
                   pub.publish(hiz)
               
           rate.sleep()

            
    def odomCallback(self,mesaj):
        self.x = mesaj.pose.pose.position.x
        self.y = mesaj.pose.pose.position.y
        mesaj.pose.pose.position.z = 0
        
        rot_q = mesaj.pose.pose.orientation
        (roll, pitch, self.theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
        
Tsp()
"""

rospy.init_node("TSP")
pub = rospy.Publisher("cmd_vel",Twist,queue_size=1)
hiz = Twist()
hedef = Point()
rate = rospy.Rate(4)

def odomCallback(mesaj):
    global x
    global y
    global theta
    x = mesaj.pose.pose.position.x
    y = mesaj.pose.pose.position.y
    mesaj.pose.pose.position.z = 0
    rot_q = mesaj.pose.pose.orientation
    
    (roll, pitch, theta) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
x = 0.0
y = 0.0
theta = 0.0
for i in range(len(koordinat)-1):
    hedef = Point()
    hedef.x = koordinat[array[i]][0]
    hedef.y = koordinat[array[i]][1]
    print("Hedef konum:")
    print(hedef)
    while not (abs(hedef.x-x)<0.01 and abs(hedef.y-y)<0.01):
        rospy.Subscriber("/odom", Odometry, odomCallback)
       
        inc_x = hedef.x - x
        inc_y = hedef.y - y
    
        aci = atan2(inc_y, inc_x)
    
        if abs(aci - theta) > 0.1:
            hiz = Twist()
            hiz.linear.x = 0.0
            hiz.angular.z = 0.3
            pub.publish(hiz)    

        else:
            hiz = Twist()
            hiz.linear.x = 0.1
            hiz.angular.z = 0.0
            pub.publish(hiz)    
        rate.sleep()
        
    print("Hedefe ulaşıldı !!!")
    
hedef.x = 0.0
hedef.y = 0.0

while not rospy.is_shutdown():
    rospy.Subscriber("/odom", Odometry, odomCallback)
    inc_x = hedef.x - x
    inc_y = hedef.y - y
    aci = atan2(inc_y, inc_x)
    
    if abs(aci - theta) > 0.1:
        hiz = Twist()
        hiz.linear.x = 0.0
        hiz.angular.z = 0.3
        pub.publish(hiz)
    else:
        hiz = Twist()
        hiz.linear.x = 0.1
        hiz.angular.z = 0.0
        pub.publish(hiz)
    rate.sleep()

print("Başlangıç noktasına dönüldü.")
