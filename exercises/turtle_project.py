"""This is my function! It draws a snowcone, and then decorates the area around it with stars, spikes, and dots - I was trying to make it like a poster, but without text. :) 
I tried to do something different by using semicircles and dots, which we didn't learn about in the turtle lesson - I found them through the documentation.
    I used these new tools in snowcone (line 47) and the dots function.
I also used randint to randomize colors and locations of different drawings, to make sure my program wasn't hard-coded! 
    I used randint in all of my functions except for snowcone, since I wanted it to be centered."""

__author__ = "_730657997_"

from turtle import Turtle, colormode, done 
from random import randint
colormode(255)


def snowCone(temp_turt: Turtle) -> None:
    """Drawing a styrofoam cup and a random-colored snowcone scoop on top."""
    temp_turt: Turtle = Turtle()

   #setting up turtle to draw a grey styrofoam cup
    temp_turt.color(180, 180, 180)
    temp_turt.speed(100000)
    temp_turt.penup()
    temp_turt.goto(-50, 100)
    temp_turt.begin_fill()
    temp_turt.setheading(100.0)
    temp_turt.pendown()
    #drawing the left side of cup
    temp_turt.forward(100)
    #turning and doing top edge
    temp_turt.right(100)
    temp_turt.forward(90)
    #turning and doing right side
    temp_turt.right(100)
    temp_turt.forward(100)
    #turning and doing bottom
    temp_turt.right(80)
    temp_turt.forward(60)
    temp_turt.end_fill()

    #setting snowcone to be random color
    temp_turt.color(randint(0, 255), randint(0, 255), randint(0, 255))
    #drawing the arch of the snowcone on top
    temp_turt.penup()
    temp_turt.speed(100000)
    temp_turt.goto(-72, 190)
    temp_turt.right(95)
    temp_turt.begin_fill()
    temp_turt.pendown()
    temp_turt.circle(-50, 170)
    temp_turt.end_fill()


def star(turt: Turtle, size: int) -> None:
    """Drawing 4 randomly located stars with the specified size."""
    turt: Turtle = Turtle()
    turt.color(254, 227, 46)
    
    idx: int = 0
    while (idx < 4):
        turt.penup()
        turt.goto(randint(-100, 100), randint(-100, 100))
        turt.speed(100000)
        turt.pendown()
        turt.setheading(60.0)
        turt.begin_fill()

        i: int = 0
        while (i < 6):
            turt.forward(size)
            turt.right(144)
            i += 1
        
        idx += 1
        turt.end_fill()


def spike(turt: Turtle, size: int) -> None:
    """This function draws a random number of stars of a specified size."""
    turt: Turtle = Turtle()
    turt.color(randint(0, 255), randint(0, 255), randint(0, 255))
    num_stars: int = randint(0, 10)
    num: int = 0
    while (num < num_stars):
        degrees: int = 0
        x_val: int = randint(-100, 100)
        y_val: int = randint(-100, 100)
        while (degrees < 360):
            turt.penup()
            turt.goto(x_val, y_val)
            turt.speed(100000)
            turt.setheading(degrees)
            turt.pendown()
            turt.forward(size)
            degrees += 60
        num += 1


def dots(turt: Turtle, amount: int) -> None:
    """This function scatters multicolored dots across the poster!"""
    turt: Turtle = Turtle()
    turt.speed(100000)

    idx: int = 0
    while (idx < amount):
        turt.penup()
        turt.goto(randint(-500, 500), randint(-500, 500))
        turt.pendown()
        turt.dot(4, randint(0, 255), randint(0, 255), randint(0, 255))
        idx += 1
    done()

def main() -> None:
    """The entrypoint of my scene. Calls all drawing functions"""
    my_turtle: Turtle = Turtle()
    snowCone(my_turtle)
    star_size: int = randint(0,100)
    star(my_turtle, star_size)
    spike(my_turtle, star_size)
    dots(my_turtle, randint(100, 200))
    done()

if __name__ == "__main__":
    main()