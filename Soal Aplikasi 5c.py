# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:55:54 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
#Cek Bilangan Bernilai Huruf
jwbulangbernilaihuruf ="y"
#nilai default jawab
while jwbulangbernilaihuruf=="y" or jwbulangbernilaihuruf=="Y":
    print ("==========================================")
    print ("       BILANGAN BULAT NILAI HURUF")
    print ("==========================================")
    u = input("--> Masukkan Bernilai Huruf = ")
    #Cek Inputan Bernilai Huruf 0 - 100 | BAIK SEKALI s/d KURANG SEKALI
    if int(u)>0 and int(u)<=100:
        if int(u)>=80:
            BernilaiHuruf= "BAIK SEKALI"
        elif int(u)>=65:
            BernilaiHuruf= "BAIK"
        elif int(u)>=55:
            BernilaiHuruf= "CUKUP"
        elif int(u)>=40:
            BernilaiHuruf= "KURANG"
        else:
            BernilaiHuruf= "KURANG SEKALI"
        print (BernilaiHuruf)
        
        #inputan jawaban dari user
        jwbulangbernilaihuruf = input("--> Mau Ulang Bernilai Huruf Lagi? y/t = ")
        if jwbulangbernilaihuruf=="t" or jwbulangbernilaihuruf=="T":
            break
    else:
        pesan="--> Masukkan Bernilai Huruf 0-100 saja"
        print(pesan)
