# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:27:05 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
#Cek Mendapat Nilai Huruf X dgn Syarat
jwbulanghuruf ="y"
#nilai default jawab
while jwbulanghuruf=="y" or jwbulanghuruf=="Y":
    print ("=================================================")
    print ("       MENDAPAT NILAI HURUF X DGN SYARAT")
    print ("=================================================")
    u = input("--> Masukkan Nilai anda dengan Huruf = ")
    #Cek Inputan Nilai Huruf X 0 - 100
    if int(u)>0 and int(u)<=100:
        if int(u)>=91:
            NilaiHuruf = "A"
        elif int(u)>=81:
            NilaiHuruf= "B"
        elif int(u)>=71: 
            NilaiHuruf= "C"
        elif int(u)>=61: 
            NilaiHuruf= "D"
        else:
            NilaiHuruf= "E"
        print (NilaiHuruf)
        
        #inputan jawaban dari user
        jwbulanghuruf = input("--> Mau Ulang Nilai Huruf Lagi? y/t = ")
        if jwbulanghuruf=="t" or jwbulanghuruf=="T":
            break
    else:
        pesan="--> Masukkan Nilai Huruf X 0-100 saja"
        print(pesan)
