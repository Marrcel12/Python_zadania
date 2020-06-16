plik= open('trojki.txt','r').readlines()
tab=[]
for  i in plik:
    tab.append(i.rstrip().split(" "))
def pierwsza(a):
    if a== 1:
        return True
    else:
        for j in range(2,a):
            if a%j==0:
                return False
        return True


for i in tab:
    suma=0
    for j in i[0]:
        suma+=int(j)
    for j in i[1]:
        suma+=int(j)
    if suma== int(i[2]):
        print(i)
print("\n")
for i in tab:
    if int(i[2])==int(i[1])*int(i[0]) and pierwsza(int(i[0]) ) and pierwsza(int(i[1])):
        print(i)
print("\n")
for i in tab:
    if int(i[0])**2+int(i[1])**2 == int(i[2])**2:
        print(i)
licznik_4=0
print("\n")
ciag_dlugosc=0
dlugosc_max=0
for i in tab:
    if int(i[0])+int(i[1])>int(i[2]) and int(i[1])+int(i[2])>int(i[0]) and int(i[0])+int(i[2])>int(i[1]):
        licznik_4+=1
        ciag_dlugosc+=1

    elif ciag_dlugosc > dlugosc_max:
        dlugosc_max=ciag_dlugosc
        ciag_dlugosc=0

    else:
        ciag_dlugosc = 0
print(licznik_4, dlugosc_max)