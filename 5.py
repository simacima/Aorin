# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 20:37:06 2019

@author: JUFRI
"""
#i=baris
#j=kolom
apa=""
i=1
x=int(input("Masukan angka"))
while i<=x:
    j=i
    while j>0:
        apa = apa + "*"
        j=j-1
        
    apa = apa + "\n"
    i = i+1
print (apa)