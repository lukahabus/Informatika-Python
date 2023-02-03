from random import randint

n = int(input())
x = int(input())

lista = []

for i in range(n):
    lista.append(randint(100, 200))

lista2 = []

for i in lista:
    if(i != x):
        lista2.append(i)

print(lista)
print(lista2)