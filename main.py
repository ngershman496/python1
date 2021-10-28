import turtle

window = turtle.Screen()
counter = 1

t1 = turtle.Turtle()
t1.speed(-1)
t1.width(5)

def drawBoard():
    t1.pu()
    t1.shape('circle')
    t1.shapesize(1)
    t1.setheading(0)
    t1.color('black')
    currentpos = -170
    for i in range(10):
        t1.setpos(-170, currentpos)
        for j in range(10):
            t1.stamp()
            t1.forward(50)
        currentpos = currentpos + 50
    t1.shape('turtle')

def up():
    t1.setheading(90)
    t1.forward(50)

def down():
    t1.setheading(270)
    t1.forward(50)

def left():
    t1.setheading(180)
    t1.forward(50)

def right():
    t1.setheading(0)
    t1.forward(50)

def blue():
    t1.color('blue')

def red():
    t1.color('red')

def switch():
    if t1.isdown():
        t1.pu()
    else:
        t1.pd()

def main():

    drawBoard()
    turtle.listen()
    turtle.onkey(up, 'w')
    turtle.onkey(down, 's')
    turtle.onkey(left, 'a')
    turtle.onkey(right, 'd')
    turtle.onkey(blue, 'b')
    turtle.onkey(red, 'r')
    turtle.onkey(switch,' ')

    window.mainloop()

main()