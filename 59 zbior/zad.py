plik=open('liczby.txt',"r+")
tab=[]
for i in plik:
    tab.append(int(i.rstrip()))
counter=0
number=0
for i in tab:
    pierwsze=[]
    dzie = 2
    if i%2!=0:
        while i>1:
            if dzie > (i/2) and  len(pierwsze)==0:
                break
            if i%dzie==0:
                i=i/dzie
                pierwsze.append(dzie)
            else:
                dzie+=1
        uniq=0
        for j in range(0,len(pierwsze)-1):
            if pierwsze[j]!= pierwsze[j+1]:
                uniq+=1
        if uniq==3:
            counter+=1
            print(counter," ",number)
    number+=1
