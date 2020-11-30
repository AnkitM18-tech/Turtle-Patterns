# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 17:22:10 2020

@author: OCAC
"""

import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(6):
    for colours in ["red","blue","cyan","magenta","green","yellow","white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()