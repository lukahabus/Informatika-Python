rijec = input()

tipke = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

broj = 0
zadnja_tipka = ''
for j in rijec: #idemo po svakom slovu zadane rijeci
    for tipka in tipke: #idemo po svakoj tipki na tipkovnici
        for i in tipka: 
            if(i == j): #ako nam se trazeno slovo nalazi na tipki
                broj += tipka.rfind(j) + 1 #zbrajamo index tipke
                if(zadnja_tipka != tipka):
                    zadnja_tipka = tipka
                else:
                    broj += 1

print(broj)