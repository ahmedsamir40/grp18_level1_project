# draw a multi circle import using turtles
# from turtle module turtle ,screen classes
import random
from turtle import Turtle, Screen

# create a turtle object from turtles class ( my_turtle)
my_turtle = Turtle()
my_turtle.speed('fast')

colors_list = ['red', 'blue', 'green', 'black', 'yellow', 'brown']

for i in range(10):
    chosen_color = random.choice(colors_list)
    my_turtle.color(chosen_color)
    my_turtle.circle(100)
    my_turtle.left(15)



my_screen = Screen()
my_screen.exitonclick()