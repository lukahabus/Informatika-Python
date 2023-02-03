n = int(input())
lista = [int(input()) for i in range(n)]
x = int(input())
y = int(input())

lista2 = []

for i in range(len(lista) + 1):
    if(i < y):
        lista2.append(lista[i])
    elif(i == y):
        lista2.append(x)
    else:
        lista2.append(lista[i - 1])

print(lista2)

# 0  1  2  3  4  5    index
#[7, 9, 8, 3, 4]      lista
#[7, 9, 8, 3, 3, 4]   lista2