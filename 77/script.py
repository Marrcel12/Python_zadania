import string

litery=list(string.ascii_uppercase)
print(litery)
plik= list (open("dokad.txt","r+").read().rstrip())
key_str=list("LUBIMYCZYTAC")
result=[]
j=0
key_time=1
for i in range(0,len(plik)):
    if j>len(key_str)-1:
        key_time+=1
        j=0
    if plik[i] in litery:
      new_index= litery.index(plik[i])+ litery.index(key_str[j])
      if new_index>25:
          new_index=new_index-26
      result.append(litery[new_index])
      j += 1
    else:
        result.append(plik[i])


# print("".join(result), "\n",key_time)



plik_szyfr=open("szyfr.txt","r+").readlines()
tab=[]
for i in plik_szyfr:
    tab.append(i.rstrip())
plik2=tab[0]
key_str2=tab[1]
result2=[]
j=0
for i in range(0,len(plik2)):
    if j>len(key_str2)-1:
        j=0
    if plik2[i] in litery:
      new_index= litery.index(plik2[i])- litery.index(key_str2[j])
      if new_index<0:
          new_index=new_index+26
      result2.append(litery[new_index])
      j += 1
    else:
        result2.append(plik2[i])
#
# print("".join(result2),"ddd")
ilosc_cal=0
ilosc=dict.fromkeys(litery)
for i in ilosc:
    ilosc[i]=0
for i in plik2:
    if i in litery:
        ilosc_cal+=1
        ilosc[i]+=1
# print(ilosc)
key_len=0
for i in ilosc:
    key_len+=ilosc[i]*(ilosc[i]-1)
d=0.0285/(key_len/(ilosc_cal*(ilosc_cal-1))-0.0385)
print(round(d,2))

