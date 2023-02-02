n = int(input())

gradovi = []

for i in range(n):
    x = int(input())
    gradovi.append(x)

km = int(input())
benzin = int(input())

lijevo = 0
for i in range(km - benzin, km + 1):
    if(i in gradovi):
        lijevo += 1

desno = 0
for i in range(km, km + benzin + 1):
    if(i in gradovi):
        desno += 1

print(max(lijevo, desno))