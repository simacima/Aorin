# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:47:31 2019

@author: JUFRI
"""
import re

kalimat = input("Masukan kalimat")
x=re.split("\s", kalimat)
print (x)
benar= False
i=0
while i != len(x) and not benar:
    y=re.findall("[0-9]", x[i])
    if (y) :
        x.remove(x[i])
    i+=1

    print ( "/" + len(x))

