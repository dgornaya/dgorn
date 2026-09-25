#!/usr/bin/python3
import turtle
turtle.speed(0)
for i in range (10000):
    x, y = turtle.pos()
    turtle.forward(1)
    turtle.setheading(30 * (x**2 + y**2)**0.5)

turtle.mainloop()
