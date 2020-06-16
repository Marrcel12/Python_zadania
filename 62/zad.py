file = open('liczby1.txt','r')
tab=[]
maks=0
min=33346
for i in file:
    tab.append(int(i,8))
    if maks<int(i):
        maks=int(i)
    if min>int(i):
        min=int(i)
print(maks,min)
file = open('liczby2.txt','r').readlines()
tab2=[]
for i in file:
    tab2.append(int(i))
dlugosci=[]
dlugosc=0
start=[]
ciagi=[]
wciagu=0
element=[tab2[0]]
for i in range(0,999):
        if tab[i]<=tab2[i+1]:
            element.append(tab2[i])
            dlugosc+=1
        else:
            element.append(tab2[i])
            ciagi.append(element)
            element=[]
            dlugosci.append(dlugosc)
            start.append(tab2[i])
ciagi.append(element)
najdluzszy=0
element=1
for i in ciagi:
    if len(i)>najdluzszy:
        najdluzszy=len(i)
        element=i[0]
print(najdluzszy,element)
liczba_takich_samych=0
wieksza=0
for i in range(0,1000):

    if tab[i]== tab2[i]:
        liczba_takich_samych+=1
    if tab[i]> tab2[i]:
        wieksza+=1
print(liczba_takich_samych,wieksza)
sze_normal=0
sze_Os=0
for i in tab2:
    for z in str(i):
        if z== '6':
            sze_normal+=1
    for z in str(oct(i)):
        if z =='6':
            sze_Os+=1
print(sze_normal,sze_Os)