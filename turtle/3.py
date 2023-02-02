import turtle

t = turtle

sqrt2 = 1.41421356237
v = 300

def square(x):
    for i in range(4):
        t.fd(x)
        t.lt(90)

def clonesquare(x):
    for i in range(4):
        c.fd(x)
        c.lt(90)

square(v)
c = t.clone()

q = v/2
for i in range(4):
    c.up()
    c.lt(45)
    c.fd(q * sqrt2 / 2)
    c.rt(45)
    c.down()
    clonesquare(q)
    q /= 2

t.left(90)
t.forward(v / 2)
t.rt(90)
n = v * sqrt2 / 2
t.rt(45)
square(n)

r = v / 2
for i in range(3):
    t.up()
    t.lt(45)
    r /= 2
    t.fd(r)
    t.down()
    n /= 2
    t.rt(45)
    square(n)

turtle.done()