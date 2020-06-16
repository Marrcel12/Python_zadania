plik=open("liczby.txt","r")
tab=[]
for line in plik:
    tab.append(int(line[:-1],2))
a=0
for liczba in tab:
    if liczba%2== 0:
        a+=1
print(a)

b=tab[0]
for liczba in tab:
    if b < liczba:
        b=liczba
print(b,bin(b)[2:])
count_9=0
sum_9=0
for liczba in tab:
    if len(str(bin(liczba))[2:])==9:
        count_9+=1
        sum_9+=liczba
print("jest ich ",count_9, "a ich suma to ",bin(sum_9)[2:])