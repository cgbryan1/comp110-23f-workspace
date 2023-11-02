"""Turtle?"""

from turtle import Turtle, colormode
leo: Turtle = Turtle()
colormode(255)

leo.color(86, 174, 246)

"""leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)
leo.left(90)
leo.forward(50)"""

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-50, 0)
leo.pendown()

leo.begin_fill()

i: int = 0
while i < 3:
    leo.forward(100)
    leo.left(120)
    i += 1

leo.end_fill()

bob: Turtle = Turtle()

bob.color(0, 0, 0)

bob.speed(500)
bob.hideturtle()

bob.penup()
bob.goto(-50, 0)
bob.pendown()

i: int = 0
while i < 3:
    bob.forward(100)
    bob.left(120)
    i += 1

side_length: int = 300
i: int = 0
while i < 100:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i += 1