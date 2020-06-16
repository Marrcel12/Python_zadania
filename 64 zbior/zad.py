plik = open("dane_obrazki.txt", "r").readlines()
tab = []

for i in range(0, 200):
    for j in range(0, 21):
        tab.append(plik[22 * i + j].rstrip())

revers = 0
max = 0
for i in range(0, 200):
    biale = 0
    czarne = 0
    for j in range(0, 20):
        for z in range(0, 20):
            if tab[21 * i + j][z] == '0':
                biale += 1
            if tab[21 * i + j][z] == '1':
                czarne += 1
    if czarne > biale:
        revers += 1
    if max < czarne:
        max = czarne
print(revers, max)
rek = 0
licznik = 0

for i in range(0, 200):
    rek = 0
    for j in range(0, 10):
        for z in range(0, 10):
            if tab[21 * i + j][z] == tab[21 * i + j + 10][z] and tab[21 * i + j][z] == tab[21 * i + j + 10][z + 10] and \
                    tab[21 * i + j][z] == tab[21 * i + j][z + 10]:
                rek += 1
    if rek == 100:
        licznik += 1

print(licznik)

naprawialne=0
popr=0
print(len(tab))
numer=[]
for i in range(0, 200):
    bledy_kol = 0
    bledy_wier = 0
    for j in range(0, 20):
        parzystosc_kol = int(tab[21 * i+20][j])
        parzystosc_wiersza = int(tab[21 * i + j][20])
        suma = 0
        print(tab[21*i+j], end=" ")

        for z in range(0, 20):
            suma += int(tab[21 * i + j][z])
        print(suma, end=" ")
        if suma % 2 == 0 and parzystosc_wiersza == 0:
            pass
            # print("parzysty")
        elif suma % 2 != 0 and parzystosc_wiersza == 1:
            pass
            # print("nieparzysy")
        else:
            bledy_wier+=1

           # print(bledy_wier,"bledyn wiersz")
        suma_kol=0
        for z in range(0,20):
            suma_kol+=int(tab[21*i+z][j])
        print('suma ' , suma_kol, 'parzystosc kol', parzystosc_kol)
        if suma_kol % 2 == 0 and parzystosc_kol == 0:
            pass
            # print("parzysty")
        elif suma_kol % 2 != 0 and parzystosc_kol == 1:
            pass
            # print("nieparzysy")
        else:
            bledy_kol += 1
            print("kol",j)
            # print(parzystosc_kol,suma_kol,bledy_kol,"bledny kol")
        # print("\n")
        # print(bledy_wier,bledy_kol,naprawialne)
    print("\n")
    if bledy_wier==0 and bledy_kol==0:
        popr+=1
    elif bledy_wier<=1 and bledy_kol<=1:
        naprawialne+=1
        # print(i)
    # print(i, "obrazek",popr)


print(naprawialne,popr)

