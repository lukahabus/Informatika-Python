n = int(input())

lista = []

for i in range(n):
    x = int(input())
    prost = 1
    for j in range(2, x):
        if(x % j == 0):
            prost = 0
    if(prost):
        lista.append(x)

print(lista)