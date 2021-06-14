# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 14:39:54 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
jwbulangnilai = "y" 
#nilai default jawab
while jwbulangnilai=="y":
    print("==============================")
    print("     CEK KELULUSAN NILAI")
    print("==============================")
    
    n = input("--> Masukkan Nilai anda = ")
    #Cek Nilai
    if int(n)>60:
        status = "LULUS"
    else:
        status = "ULANG"
        
    print(status)
    
    #input jawab dari user
    jwbulangnilai = input("--> Mau Ulang Cek Lagi? y/t = ")
    if jwbulangnilai=="t":
        break
