wiadomosci= open("wiadomosci.txt","r+").read().split("\n")

podpisy= open("podpisy.txt","r+").read().split("\n")
print(wiadomosci)
print(podpisy)
skroty=[]
def skrot(wiadomosc):
    S=[ord("A"),ord("L"),ord("G"),ord("O"),ord("R"),ord("Y"),ord("T"),ord("M")]

    while len(wiadomosc) % 8 !=0:
        wiadomosc+="."
    print(len(wiadomosc))
    j=0
    for i in wiadomosc:
        if j==8:
            j=0
        S[j]= (S[j]+ord(i))%128
        j+=1
    print(S)
    wynik=""
    for j in range(8):
        wynik+=chr(65+S[j]%26)
    return wynik

for wiad in wiadomosci:
    skroty.append(skrot(wiad))
def A(podpis):
    wynik=""
    for i in podpis:

        x=(int(i)*3%200)
        wynik+=chr(x)
    return wynik
podpisy_skroty=[]
for podpis in podpisy:
    podpisy_skroty.append(A(podpis.split(" ")))
for i in range(11):
    if (podpisy_skroty[i]==skroty[i]):
        print("wiad ",i+1, "wiarygodnia")
    else:
        print("wiad ", i+1 , "nie_wiarygodna")
