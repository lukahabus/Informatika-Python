n = int(input())
m = int(input())

#5 3
#1 2 3 4 5
#4 5 1 2
#2 4 5
#2 4
#4

lista = []
for i in range(n):
    lista.append(i + 1)

while(len(lista) > 1):
    lista2 = []
    for i in range(m + 1, m + len(lista)):
        x = i % n
        if(x == 0):
            x = n
        lista2.append(x)
    del lista[0]
    for i in lista2:
        lista.append(i)
        del lista[0]
    
print(lista[0])