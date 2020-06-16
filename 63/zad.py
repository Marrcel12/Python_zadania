plik= open('ciagi.txt','r').readlines()
dwu=[]

for i in plik:
    i.rstrip()
for i in plik:
    dl=(len(str(i))-1)/2
    if dl.is_integer():
        dl=int(dl)
        if int(str(i)[:dl]) == int(str(i)[dl:]):
            dwu.append(int(i))
print(dwu)
brak_1=0
for i in plik:
    flag=1
    for j in range(2,len(str(i))):
       if i[j-2] == i[j-1] =='1' or i[j]== i[j-1] =='1':
           flag=0
    if flag==1:
        brak_1+=1
print(brak_1)
print("\n")
def pierwsza(a):
    if a >1:
        for i in range(2, a//2):
            if a%i==0:
                return False
        else:
            return True
maks_polpierw=0
min_polpierw=18
ilosc=0

for i in plik:
    tab_of_prime=[]
    liczba= int(i,2)
    for a in range(1,liczba):
            if liczba%a==0:
                tab_of_prime.append(a)
                liczba=liczba/a

    if len(tab_of_prime)==3:

        if pierwsza(tab_of_prime[1]) and pierwsza(tab_of_prime[2]) and tab_of_prime[1]*tab_of_prime[2]==int(i,2):

                        ilosc+=1
                        if maks_polpierw<int(i,2):
                            maks_polpierw=int(i,2)
                        if min_polpierw>int(i,2):
                            min_polpierw=int(i,2)
print(ilosc,min_polpierw,maks_polpierw)
