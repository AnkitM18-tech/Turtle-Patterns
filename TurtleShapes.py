# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:10:30 2020

@author: OCAC
"""

import turtle
import time

trtl=turtle.Turtle()
trtl.pencolor("blue")
trtl.pensize(5)
trtl.shape("turtle")
n=3
shapes=["Triangle","Square","Pentagon","Hexagon","Octagon"]
while n<9:
    trtl.clear()
    for i in range(n):
        trtl.pencolor("blue")
        trtl.forward(60)
        trtl.right(360/n)
    n+=1
    trtl.penup();trtl.home();trtl.pendown();trtl.penup();trtl.home()
    trtl.pendown();trtl.ht();time.sleep(1);trtl.st()