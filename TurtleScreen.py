import turtle as tu
import random as rd
import time as t

def inside_window():
    left_limit=(-tu.window_width()/2)+100
    right_limit=(tu.window_width()/2)-100
    upper_limit=(tu.window_height()/2)-100
    bottom_limit=(-tu.window_height()/2)+100
    (x,y)=tu.pos()
    inside=left_limit < x < right_limit and bottom_limit < y < upper_limit
    return inside

def move_turtle():
    if inside_window():
        angle=rd.randint(0,180)
        #dist=rd.randint(50,300)
        tu.right(angle)
        tu.forward(200)
    else:
        tu.backward(200)

tu.penup()
tu.shape("turtle")
tu.fillcolor("blue")
tu.bgcolor("white")
tu.speed("slow")

while True:
    move_turtle()
