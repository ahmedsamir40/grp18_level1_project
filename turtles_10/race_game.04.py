# from turtle module import Turtle class, Screen class
import random
import time
from turtle import Turtle, Screen
# take object from turtle class
my_turtle = Turtle()
def draw_turtle(turtle_name, turtle_color, y_pas):
turtle_name = Turtle()
turtle_name.color(turtle_color)
turtle_name.shape('turtle')
turtle_name.shapesize(1.5)
turtle_name.penup()
turtle_name.goto(x=-300,y=y_pas)
turtle_name.pendown()
return turtle_name
# take object from Screen class

my_screen = Screen()

# screen setup
my_screen.title('race game')
my_screen.setup(800,500)
my_screen.bgcolor('forestgreen')


# heading
my_turtle.penup()
my_turtle.goto(-100,205)
my_turtle.color('white')
my_turtle.write('Turtle Race', font=('Arial',20,'bold'))

#  brown floor
my_turtle.goto(-350, 200)
my_turtle.pendown()
my_turtle.color('black')
my_turtle.fillcolor('chocolate')

my_turtle.begin_fill()
for i in range(2):
    my_turtle.forward(700)
    my_turtle.right(90)
    my_turtle.forward(400)
    my_turtle.right(90)
my_turtle.end_fill()

# finish line (temp)
my_turtle.penup()
my_turtle.goto(250,200)
my_turtle.right(90)
my_turtle.pendown()
my_turtle.forward(400)



# draw Turtles
# blue turtles
b_turtle = draw_turtle(turtle_name='blue_turtle',turtle_color='cyan',y_pas = 150)
p_turtle = draw_turtle(turtle_name='pink_turtle',turtle_color='pink',y_pas = 50)
y_turtle = draw_turtle(turtle_name='yellow_turtle',turtle_color='yellow',y_pas = -50)
g_turtle = draw_turtle(turtle_name='green_turtle',turtle_color='green',y_pas = -150)

#pause for 1 second before start the race
time.sleep(1)
#keyboard.listener
my_screen.listener
my_screen.onkey(control_turtle,'kight')

#move the turtles
while True:
    b_turtle.forward(random.randint(1,10))
    p_turtle.forward(random.randint(1,10))
    y_turtle.forward(random.randint(1,10))
    # g_turtle.forward(random.randint(1,10))
    if b_turtle.xcor > 230:
        winner = b_turtle
        break
    if p_turtle.xcor > 230:
        winner = p_turtle
        break
    if y_turtle.xcor > 230:
        winner = y_turtle
        break
    if g_turtle.xcor > 230:
        winner = g_turtle
        break
#celebrate the winner
winner.shapesize(2,5)
for i in range(1000):
    winner.left(5)
my_screen.exitonclick()

