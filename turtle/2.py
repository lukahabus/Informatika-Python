import turtle

t = turtle

v = 200

def halfsquare(x):
    for i in range(2):
        t.fd(x)
        t.lt(90)

def square(x):
    for i in range(4):
        t.fd(x)
        t.lt(90)

def kvadrati(x):
    square(x)
    t.fd(x)
    x /= 2
    square(x)
    x *= 2
    t.lt(90)
    halfsquare(x)
    t.lt(90)
    x /= 2
    square(x)

def nacrtaj(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    kvadrati(v)

t.backward(400)
kvadrati(v)

v /= 4
for i in range(0, 4):
    nacrtaj(-400 + 100 * i, 300 - 100 * i)

turtle.done()