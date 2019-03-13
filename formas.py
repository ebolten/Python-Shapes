#Practicing with Turtle!
import turtle
my_turtle = turtle.Turtle()
my_turtle.speed(0)

def square():
    for i in range(4):
        my_turtle.forward(70)
        my_turtle.left(90)
def triangle():
    for i in range(3):
        my_turtle.left(120)
        my_turtle.forward(100)
def circle_squares():
    for i in range(120):
        square()
        my_turtle.right(3)

def circle_triangles():
    for i in range(120):
        triangle()
        my_turtle.left(3)

def circle_cirlces():
    for i in range(120):
        my_turtle.circle(50)
        my_turtle.right(3)

def heart():
    def curvemove():
        for i in range(200):
            my_turtle.right(1)
            my_turtle.forward(1)
    my_turtle.left(140)
    my_turtle.forward(111.65)
    curvemove()
    my_turtle.left(120)
    curvemove()
    my_turtle.forward(111.65)

my_turtle.penup()
my_turtle.goto(-150,0)
my_turtle.pendown()

circle_squares()

my_turtle.penup()
my_turtle.goto(100,-100)
my_turtle.pendown()

circle_triangles()

my_turtle.penup()
my_turtle.goto(60,150)
my_turtle.pendown()

circle_cirlces()

my_turtle.penup()
my_turtle.goto(-200,200)
my_turtle.pendown()

end = input('Press Enter to Close')









