# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:42:52 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
#Cek Golongan Usia
jwbulangprogram ="y"
#nilai default jawab
while jwbulangprogram=="y" or jwbulangprogram=="Y":
    print ("=============================")
    print ("       KATEGORI USIA")
    print ("=============================")
    u = input("--> Masukkan Usia = ")
    #cek batasan inputan usia 0-100
    if int(u)>0 and int(u)<=100:
        if int(u)>=60:   status= "Lansia"
        elif int(u)>=35: status= "Dewasa"
        elif int(u)>=18: status= "Pemuda"
        elif int(u)>=15: status= "Remaja"
        else:
            status="Anak"
        print (status)
        
        #inputan jawab dari user
        jwbulangprogram = input("--> Mau Ulang Program Lagi? y/t = ")
        if jwbulangprogram=="t" or jwbulangprogram=="T":
            break
    else:
        pesan="--> Masukkan angka usia 0-100 saja"
        print(pesan)