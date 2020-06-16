import math
file= open('dane_systemy1.txt',"r").readlines()
s1=[]
for i in file:
    s1.append(i.rstrip().split(" "))

max_s1="0"
for i in s1:
    if int(max_s1,2) > int(i[1],2):
        max_s1=i[1]
print(max_s1)

file= open('dane_systemy2.txt',"r").readlines()
s2=[]
for i in file:
    s2.append(i.rstrip().split(" "))

max_s2="0"
for i in s2:
    if int(max_s2,4) > int(i[1],4):
        max_s2=i[1]
print(str(bin(int(max_s2,4))).replace('0b',""))

file= open('dane_systemy3.txt',"r").readlines()
s3=[]
for i in file:
    s3.append(i.rstrip().split(" "))

max_s3="0"
for i in s3:
    if int(max_s3,8) > int(i[1],8):
        max_s3=i[1]
print(str(bin(int(max_s3,8))).replace('0b',""))
# 2
licznik=0
for i in range(0,1095):
    wartosc= 12 + i*24
    if (wartosc != int(s1[i][0],2)) and (wartosc != int(s2[i][0],4)) and (wartosc != int(s3[i][0],8)):
        licznik+=1
print(licznik)
# 3
tym_max_1=int(s1[0][1],2)
tym_max_2=int(s1[0][1],4)
tym_max_3=int(s1[0][1],8)
rek_dzien=0
for i in range(1,1095):
    if int(s1[i][1],2) > tym_max_1 or int(s2[i][1],4) > tym_max_2 or int(s3[i][1],8)> tym_max_3:
        if int(s1[i][1],2) > tym_max_1:
            tym_max_1= int(s1[i][1],2)
        if int(s2[i][1], 4) > tym_max_2:
            tym_max_2 = int(s2[i][1], 4)
        if int(s3[i][1], 8) > tym_max_3:
            tym_max_3 = int(s3[i][1], 8)
        rek_dzien+=1
print(rek_dzien)
max=0

for i in range(0,1093):
        for j in range(i+1, 1093):
            kwa= (int(s1[i][1],2)-int(s1[j][1],2))**2
            skok= math.ceil(kwa/abs(j-i))
            if max< skok:
                max=skok
print(max)



