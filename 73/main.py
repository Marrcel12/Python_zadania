plik= open("tekst.txt","r").read().rstrip()
tab=plik.split(" ")
print(tab)
licznik=0
for i in tab:
    powtorze=0
    for z in range(1,len(i)-1):
        if i[z-1]==i[z] or i[z]==i[z+1]:
            powtorze+=1
    if powtorze>0:
        licznik+=1
print(licznik)
alph="abcdefghijklmnopqrstuvwxyz".upper()
dic=dict.fromkeys(alph,0)
all=0
for i in tab:
    for z in i:
        dic[z]+=1
        all+=1


for i in dic:
    print(i, dic[i] ,"(",round(dic[i]/all*100,3),"%)")

def spolgloski(a):
    max=0
    s=0
    for i in a:
        if i== "A" or i=="E" or i=="O" or i== "U" or i=="I" or i == "Y":
            s=0
        else:
            s+=1
        if s > max:
            max =s
    return max
pierwsze=""
maks=0
ilosc_max=0
for i in tab:
    if maks < spolgloski(i):
        maks= spolgloski(i)
        ilosc_max=1
        pierwsze= i
    elif spolgloski(i)== maks:
        ilosc_max+=1
print(pierwsze, maks,ilosc_max)