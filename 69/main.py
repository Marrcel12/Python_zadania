file=open("dane_geny.txt").readlines()
tab=[]
for i in file:
    tab.append(i.rstrip())
print(tab)
dicOfLen={}

for i in file:
    try:
        dicOfLen[len(i)]+=1
    except:
        dicOfLen[len(i)]=1
print(dicOfLen)

licznik=len(dicOfLen)
najwiecej=0
for key in dicOfLen:
    if najwiecej< dicOfLen[key]:
        najwiecej=dicOfLen[key]
print("zad1",licznik,najwiecej)
# zad2
licznik=0
gens=[]
start=None
for indx,i in enumerate(tab):
    gens.append([])
    start = None
    for z in range(len(i)-1):
        if (i[z],i[z+1])==("A","A") and start==None:
            start=z
        if (i[z],i[z+1])==("B","B") and start!=None:
            end=z+2
            gens[indx].append(i[int(start):int(end)])
            start=None

print(gens)
for i in gens:
    for z in i:
        if "BCDDC" in z:
            licznik+=1
            break
print("zad2 ",licznik)

najwieksza_ilosc=0
najwikeszy_gen=0
for i in gens:
   if len(i)>najwieksza_ilosc:
        najwieksza_ilosc= len(i)

   for z in i:
       if len(z)> najwikeszy_gen:
           najwikeszy_gen=len(z)

print("zad3", najwieksza_ilosc, najwikeszy_gen)
silnie_odp=0
for i in tab:

    if i==i[::-1]:
        silnie_odp+=1

odp=0
czesc_kod_list=[]
for i in gens:
    czesc_kod=""
    for z in i:
        czesc_kod+=z
    czesc_kod_list.append(czesc_kod)



#
gens2=[]
for indx,i in enumerate(tab):
    a=i[::-1]
    gens2.append([])
    start = None
    for z in range(len(a)-1):
        if (a[z],a[z+1])==("A","A") and start==None:
            start=z
        if (a[z],a[z+1])==("B","B") and start!=None:
            end=z+2

            gens2[indx].append(a[int(start):int(end)])
            start=None
print(gens2)
czesc_kod_list2=[]
for i in gens2:
    czesc_kod=""
    for z in i:
        czesc_kod+=z
    czesc_kod_list2.append(czesc_kod)
for i in range(len(czesc_kod_list)):
    if czesc_kod_list[i]== czesc_kod_list2[i]:
        odp+=1
print(odp,silnie_odp)