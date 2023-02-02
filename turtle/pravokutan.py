import turtle

s = turtle.getscreen()

t = turtle.Turtle()

x = 0
y = 0

def pravokutnik(a, b):
    for i in range(2):
        t.fd(a)
        t.lt(90)
        t.fd(b)
        t.lt(90)

def ladica(n, a, b, d, x, y):
    for i in range(n):
        pravokutnik(a, b)
        y = y + b + d
        t.penup()
        t.goto(x, y)
        t.pendown()

def ladice(x, y):
    for broj in l:
        ladica(broj, a, b, d, x, y)
        x += a + 4 * d
        t.penup()
        t.goto(x, y)
        t.pendown()

a = int(input('unesi a\n'))
b = int(input('unesi b\n'))
d = int(input('unesi d\n'))
n = 3
l = [3, 1, 5, 2, 4, 1, 2]

ladice(0, 0)

turtle.done()