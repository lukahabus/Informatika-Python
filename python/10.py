n = int(input())
koef = [int(input()) for i in range(n + 1)]

slobo = koef[-1]

for j in range(-slobo, slobo + 1):
    if j != 0 and slobo % j == 0:
        y = 0
        pot = n
        for i in range(len(koef)):
            y += koef[i] * j ** pot
            pot -= 1
        if y == 0:
            print(j)