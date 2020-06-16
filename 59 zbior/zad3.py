plik=open('liczby.txt',"r+")
tab=[]
def iloczyn(numbers):
    to_return=1
    for i in str(numbers):
        to_return*= int(i)
    return to_return

for i in plik:
    tab.append(int(i.rstrip()))
dic={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
max=0
min=999999
for i in tab:
    counter = 0
    number=i
    while i>9:
        i=iloczyn(i)
        counter+=1
    dic[counter]+=1
    if counter==1:
        if number >max:
            max=number
        if number < min:
            min=number
print(dic," " ,max, " ",min )
