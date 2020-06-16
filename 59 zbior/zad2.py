plik=open('liczby.txt',"r+")
tab=[]
for i in plik:
    tab.append(int(i.rstrip()))
count=0
for i in tab:
   reve = int(str(i)[::-1])
   sum=i+reve
   if sum == int(str(sum)[::-1]):
    count+=1

print(count)

