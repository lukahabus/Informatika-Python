from random import randint

n = int(input())

lista = []

for i in range(n):
    lista.append(randint(100, 200))

lista2 = []

for i in range(n):
    lista2.append(lista[n - i - 1])

print(lista)
print(lista2)