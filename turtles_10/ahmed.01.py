from turtle import Turtle, Screen

my_tutle = Turtle()
my_tutle.shape('turtle')
my_tutle.color('black')
my_tutle.fillcolor('green')

my_tutle.begin_fill()
for i in range(2):
    my_tutle.forward(250)
    my_tutle.left(90)
    my_tutle.forward(200)
    my_tutle.left(90)
my_tutle.end_fill()
my_tutle.penup()
my_tutle.goto(-200,100)
my_tutle.shape('square')
my_tutle.stamp()
for i in range(2):
    my_tutle.forward(100)
    my_tutle.stamp()

my_tutle.shape('turtle')
my_tutle.goto(-100,-200)
my_tutle.pendown()
my_tutle.circle(50)



my_screen = Screen()
my_screen.exitonclick()