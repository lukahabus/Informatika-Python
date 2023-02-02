import turtle

s = turtle.getscreen()

t = turtle.Turtle()

def kvadrat(d):
    for i in range(4):
        t.fd(d)
        t.lt(90)

def linije(d):
    t.goto(0, d/2)
    t.fd(d)
    t.penup()
    t.goto(d/2, 0)
    t.pendown()
    t.lt(90)
    t.fd(d)
    t.penup()
    t.goto(0, 0)
    t.rt(90)
    t.pendown()

d = int(input('unesi d\n'))
n = int(input('unesi n\n'))

kvadrat(d)
for i in range(n):
    linije(d)
    d = d/2

turtle.done()