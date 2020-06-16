def pierwsza(a):
    for i in range(a, 300):
        flag=1
        for u in range(2,int(a)//2+1):
            if i % u == 0:
                flag=0
                break
        if flag==1:
            return i

stan={"200":2000, "100":2000,"50":2000,"20":500,"10":500}
niedostarczone={"200":0, "100":0,"50":0,"20":0,"10":0}
def dostawa():
    global stan, niedostarczone
    for i in stan.keys():
        stan[i]+=pierwsza(int(i))*40+70
        # 59
        if i == "200":
            if stan[i]> 15000:
                niedostarczone["200"]=+stan[i]-15000
                stan[i]=15000
        if i == "100":
            if stan[i] > 10000:
                niedostarczone["100"]=+stan[i]-10000
                stan[i] =10000
        if i == "50":
            if stan[i] > 7500:
                niedostarczone["50"]=+stan[i]-7500
                stan[i] =7500
        if i == "20":
            if stan[i] > 5000:
                niedostarczone["20"]=+stan[i]-5000
                stan[i] =5000
        if i == "10":
            if stan[i] > 2500:
                niedostarczone["10"]=+stan[i]-2500
                stan[i] =2500
# print(stan)
file=open('transakcje.txt','r').readlines()
tranzakcje=[]
for i in file:
    tab=[]
    for z in i.split():
       tab.append(int(z))
    tranzakcje.append(tab)

# print(tranzakcje)
def wyplacanie(suma):
    global stan
    while suma  - 200 >=0 and stan['200']>0 and suma>0:
        suma -= 200
        stan["200"]-=1
    while suma - 100 >= 0and suma>0 and stan['100']>0:
        suma -=100

        stan["100"]-=1
    while suma - 50 >=0and suma>0 and stan['50']>0 :
        suma -=50
        stan["50"]-=1
    while suma - 20 >=0 and suma>0 and stan['20']>0:
        suma -= 20
        stan["20"]-=1
    while suma - 10 >=0 and suma>0 and stan['10']>0:
        suma -= 10
        stan["10"]-=1

vip_zre=0
vip_od=0
flagvip=0
vip=False
flag=1
for i in tranzakcje:
    numer = i[0]
    kwota = i[1]
    if kwota>9000:
        vip=True
    for j in stan.keys():
        if stan[j]<3:
            flag=0
    if numer % 500==0:
            dostawa()
            flag=1
    if flag==1:
        vip_zre+=1
        wyplacanie(kwota)
        print(stan)

    else:
        vip_od += 1
sum=0
for i in stan:
    sum+=stan[i]*int(i)
print("wartosc",4200000)
print("wartosc",sum)
print(vip_zre, vip_od)
print(niedostarczone)