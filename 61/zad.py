
plik=open('ciagi.txt').readlines()
tab=[]
element=[]
flag=0
for i in range(0,200):
    if i %2!=0:
        element.append(plik[i].rstrip().split())
    else:
        tab.append(element)
        element=[]
        element.append(plik[i].rstrip())
tab.append(element)
tab.pop(0)
# print(tab)
r_max=0
aryt=0
for i in tab:
    n=int(i[0])
    a_1=int(i[1][0])
    r= int(i[1][1])-int(i[1][0])
    sum=((2*a_1)+(n-1)*r)/2*n
    sum_pret=0
    for z in i[1]:
        sum_pret+=int(z)
    if sum_pret == sum:
        aryt+=1
        if r_max< r:
            r_max=r
#print(r_max, aryt)
def szescain(a):
    for v in range(0,a):
        if v*v*v== a:
            return True

    return False

counter=0
to_print=[]
for i in tab:
    lisst=[]
    for o in i[1]:
        lisst.append(int(o))
    lisst.sort(reverse=True)
    for z in lisst:
        if szescain(z):
            print(z)
            to_print.append(z)
            break
    counter+=1
    print(counter)
print(to_print)
