file= open("hasla.txt","r").readlines()
tab=[]
for i in file:
    tab.append(i.rstrip())

# zad1
zad1=0
for i in tab:
    try:
        int(i)
    except ValueError:
        continue
    zad1+=1
print(zad1)

# zad2
zad2=[]
for i in tab:
    licznik=0
    for j in tab:
        if i==j:
            licznik+=1
            if licznik==2:
                zad2.append(i)
                break
zad2=sorted(list(dict.fromkeys(zad2)))
# print(sorted(zad2))
# zad2D=[]
# for i in zad2:
#     if i not in zad2D:
#         zad2D.append(i)
print(zad2)

zad3=0
for i in tab:
    licznik=0
    for j in range(0, len(i)):
        test_lett=[]
        for z in i[j:j+4]:
            test_lett.append(ord(z))
        test_lett.sort()
        # print(test_lett)
        if len(test_lett)==4:
            if test_lett[3]-test_lett[2]==1 and test_lett[2]-test_lett[1]==1 and test_lett[1]-test_lett[0]==1:
                # print(i)
                zad3+=1
                break
print(zad3)


# zad4
licznikzad4=0
for passw in tab:
    point=[0,0,0]
    for i in range(0,10):
        if str(i) in passw:
            point[0]=1
    for i in passw:
        if i.isupper():
            point[1]=1
        if i.islower():
            point[2]=1
    if point== [1,1,1]:
        licznikzad4+=1
print(licznikzad4)