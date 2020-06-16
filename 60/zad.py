plik=open("liczby.txt",'r').readlines()

tab=[]
for i in plik:
    i=i.rstrip()
    tab.append(int(i))

mniejszych_1000= 0
liczby=[]
for i in tab:
    if i < 1000:
        mniejszych_1000+=1
        liczby.append(i)
print(mniejszych_1000,liczby[-2],liczby[-1])
dziel=0
dzielniki=[]
z=10
counter=0
for z in tab:
    tab_of_=[]
    for i in range(1, z+1):
        if z%i==0:
            tab_of_.append(i)
    if len(tab_of_)== 18:
        dziel+=1
        dzielniki.append(tab_of_)
print(dziel,dzielniki)
liczby_nwd_1=[]
def nwd(a, b):
    while b:
        a, b = b, a%b
    return a
for i in tab:
    flag=1
    for k in range(0,200):
        if nwd(i, tab[k])!=1 and i !=tab[k]:
          flag=0

    if flag==1:
        liczby_nwd_1.append(i)

maks_liczby_nwd=0

for i in liczby_nwd_1:
    if maks_liczby_nwd < i:
        maks_liczby_nwd=i
print(maks_liczby_nwd)


