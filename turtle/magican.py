import turtle

s = turtle.getscreen()

t = turtle.Turtle()

r = 100

def krilo(d):
    t.lt(30)
    t.fd(d)
    t.rt(60)
    t.fd(d)
    t.rt(120)
    t.fd(d)
    t.rt(60)
    t.fd(d)
    t.bk(d)
    t.rt(60)
    t.fd(d)

def prebaci(pos):
    t.setheading(0)
    t.penup()
    t.goto(0, pos)
    t.pendown()

def zarotiraj(kut):
    t.lt(kut)
    t.penup()
    t.fd(r)
    t.pendown()

t.circle(r)
prebaci(r/3)
t.circle(r * 2/3)
prebaci(r)

zarotiraj(45)
krilo(100)
prebaci(r)

zarotiraj(135)
krilo(100)
prebaci(r)

zarotiraj(210)
krilo(60)
prebaci(r)

zarotiraj(330)
krilo(60)
prebaci(r)

turtle.done()