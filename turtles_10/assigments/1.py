from turtle import Turtle, Screen

my_turtle = Turtle()

for i in range(3, 10):
    num_of_sides = i
    angle = 360 / num_of_sides
    for i in range(i):
        my_turtle.forward(100)
        my_turtle.left(angle)





my_screen = Screen()
my_screen.exitonclick()