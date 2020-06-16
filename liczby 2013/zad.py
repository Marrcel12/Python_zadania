file= open("dane.txt","r").read().split("\n")
a=0
for liczba in file:
    if liczba[0]==liczba[len(liczba)-1]:

        a+=1
print(a)
b=0
for liczba in file:
    liczba=str(int(liczba,8))
    if liczba[0]==liczba[len(liczba)-1]:
        b += 1
print(b)

c_max=447
c_min=447
c=0
for liczba in file:
    flag=1
    liczba=int(liczba)
    for i in range(0,len(str(liczba))-1):
        if str(liczba)[i] > str(liczba)[i+1]:
            flag=0

    if flag ==1:
        c += 1
        if c_max < liczba:
            c_max=liczba
        if c_min > liczba:
            c_min=liczba
print(c_min, " ",c_max, c)