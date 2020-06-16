plik=open('bledne.txt').readlines()
tab=[]
element=[]
flag=0
for i in range(0,40):
    if i %2!=0:
        element.append(plik[i].rstrip().split())
    else:
        tab.append(element)
        element=[]
        element.append(plik[i].rstrip())
tab.append(element)
tab.pop(0)
print(tab)
bledy=[]
for i in range(0,20):
    roznica=0
    roznica_obecna=0
    print(int(tab[i][0]))
    for k in range(0,int(tab[i][0])-1):
        if k == 0:
            if int(tab[i][1][k+1])-int(tab[i][1][k]) == int(tab[i][1][k+2])-int(tab[i][1][k+1]):
                roznica=int(tab[i][1][k+1])-int(tab[i][1][k])
            else:
                roznica= int(tab[i][1][k+3])-int(tab[i][1][k+2])
        roznica_obecna==int(tab[i][1][k+1])-int(tab[i][1][k])
        if roznica_obecna != roznica:
            bledy.append(tab[i][1][k])
print(bledy)