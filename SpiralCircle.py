import turtle as tu
colors=["red","purple","blue","green","yellow","orange"]
tu.bgcolor("white")

for x in range(360):
    tu.pencolor(colors[x%6])
    tu.width(x/100+1)
    tu.forward(x)
    tu.left(59)   