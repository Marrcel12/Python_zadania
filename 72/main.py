plik= open("napisy.txt","r").readlines()
tab=[]
for i in plik:
    tab.append(i.rstrip().split(" "))
licznik_1=0
pierwsza=""
flag=0
for i in tab:
    if len(i[0]) >= len(i[1])*3 or len(i[1]) >= len(i[0])*3:
        licznik_1+=1
        if flag==0:
            pierwsza=i
            flag=1
print(licznik_1,pierwsza)

for i in tab:
    if(len(i[1])-len(i[0])) >0 and i[0] == i[1][:len(i[0])]:
        print(i, "/", i[1][len(i[0]):]," / ", )
max=0
list_of_max=[]
for i in tab:
    temp_max=0
    kraniec=0
    if len(i[0])> len(i[1]):

        stop= len(i[1])*-1
    else:

        stop= len(i[0])*-1
    for z in range(-1,stop-1, -1):
        if i[1][z]== i[0][z]:

            temp_max+=1
        else:
            break
    if temp_max>max:
        max=temp_max
        list_of_max=[]
    if temp_max==max:
        list_of_max.append(i)

print(max, list_of_max)
