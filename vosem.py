#!/usr/bin/python3
import turtle
turtle.shape('turtle')

def circle(direction='left'):
    N = 200
    for i in range(N):
        turtle.forward(1)
        if direction == "left":
            turtle.left(360 / N)
        elif diection == "right":
            turtle.right(360 / N)
        else:
            print("oshibksa")
            return

def eight():
    circle('left')
    circle('right')

turtle.speed(0)

eight()

turtle.mainloop()


