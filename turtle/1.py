import turtle

s = turtle.getscreen()

t = turtle.Turtle()

v = 80

def square():
    for i in range(4):
        t.fd(v)
        t.lt(90)

t.goto(-450, 0)

for i in range(5):
    square()
    t.fd(v)
    v += 10

v -= 10

for i in range(4):
    v -= 10
    square()
    t.fd(v)

turtle.done()