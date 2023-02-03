n = int(input())
lista = [int(input()) for i in range(n)]
x = int(input())

lista2 = []

for i in lista:
    if(i != x):
        lista2.append(i)

print(lista2)