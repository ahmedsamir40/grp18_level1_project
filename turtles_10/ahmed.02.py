import random
from turtle import Turtle,Screen
my_turtle = Turtle()
my_turtle.speed('fast')
colors_list = ['red', 'yellow', 'green', 'black', 'blue', 'brown']

for i in range(10):
    my_turtle.color(random.choice(colors_list))
    my_turtle.circle(100)
    my_turtle.left(15)

my_screen = Screen()
my_screen.exitonclick()