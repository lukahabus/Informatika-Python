# 4 pravokutnika duzine a = 100 b = 50

import turtle

s = turtle.getscreen()

t = turtle.Turtle()

a = 100
b = 50

def pravokutnik():
    t.fd(a)
    t.lt(90)
    t.fd(b)
    t.rt(90)

for i in range(4):
    pravokutnik()

t.lt(180)

for i in range(4):
    pravokutnik()

turtle.done()