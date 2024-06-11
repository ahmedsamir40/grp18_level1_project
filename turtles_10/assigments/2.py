from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape('turtle')
colors_list = ['red', 'green', 'blue', 'yellow', 'darkgreen']
angles_list = [0, 90, 180, 270]
my_turtle.pensize(5)
my_turtle.speed('slowest')

for i in range(200):
    my_turtle.color(random.choice(colors_list))
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(angles_list))

my_screen = Screen()
my_screen.exitonclick()