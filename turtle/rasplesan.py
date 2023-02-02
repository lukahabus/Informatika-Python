import turtle

s = turtle.getscreen()

t = turtle.Turtle()

t.lt(90)

d = int(input('unesi d\n'))
kut = int(input('unesi kut\n'))
n = int(input('unesi n\n'))

for i in range(n):
    if((i + 1) % 3 != 0):
        t.fd(d)
        t.rt(kut)
    else:
        t.bk(d)
        t.lt(kut)

turtle.done()