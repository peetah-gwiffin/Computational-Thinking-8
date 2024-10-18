import turtle


t = turtle.Turtle()

t.penup()

t.goto(100,0)
t.pendown()
t.color("red")

#circle 1

for i in range(400):
    t.forward(2)
    t.left(1.1)
   #transition 

t.penup()

t.goto(-100,0)
t.pendown()
t.color("red")

#second circle

for i in range(300):
    t.forward(2)
    t.left(1.1)