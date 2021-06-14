# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 18:32:30 2021

@author: Tio Chalil Gibran Findianto | 20083000152 - 2E
"""
jwbulangharga ="y"
#nilai default jawab
while jwbulangharga=="y" or jwbulangharga=="Y":
    print ("=====================================================")
    print ("       TRANSAKSI PEMBELIAN PRINTER EPSON T20")
    print ("=====================================================")
        
    #Cek Nilai Awal Variable JmlBeli = Harga 1 Printer
    HargaPrint = 660000
    JikaNilaiBeliDiAtas = 1500000
    Diskon = 15 
    
    #Inputan Jumlah Beli
    print ("--> TRANSAKSI PEMBELIAN PRINTER EPSON T20 <--")
    JmlBeli = input ("Jumlah Printer Epson T20 yang dibelikan = ")
    
    #Proses Hitung Total
    Total = int(HargaPrint) * int(JmlBeli) / int(Diskon)
    
    #Tampilkan Total Biaya
    print ("Total Transaksi Pembelian Printer Epson T20 = Rp. " + str (Total))
    
    #Inputan jawaban dari user
    jwbulangharga = input("--> Mau Beli Lagi? y/t = ")
    if jwbulangharga=="t" or jwbulangharga=="T":
            break
