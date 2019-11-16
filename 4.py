# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 19:33:37 2019

@author: JUFRI
"""

def my_function(cocok):
    for i in range (len(cocok)):
        for k in range (i+1, len(cocok)):
            text= "terdapat {} pasang {},"
            if cocok[i]==cocok[k]:
                print (text.format(2,cocok[i]))
                i=i+1
        
dicocok = [1,5,1,7,8,6,8,9,4,5]
my_function(dicocok)
