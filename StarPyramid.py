# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 01:05:57 2020

@author: OCAC
"""

n=int(input("enter no of rows:"))

for i in range(1,n+1):
    for j in range(i):
        print("* ",end="")
    print()  
    
for x in range(n-1,0,-1):
    for y in range(x):
        print("* ",end="")
    print()  