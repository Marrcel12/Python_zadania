file= open("tekst.txt","r").read()
tab=file.split()
for i in tab:
        if i[0]=="d" and i[-1]=="d":
            # print(i)
            pass

dict={"a":0, "b":1, "c":2, "d":3,"e":4,"f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13,"o":14, "p":15, "q":16, "r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
dict_keys=list(dict.keys())
dict_val=list(dict.values())
for i in tab:
    if len(i)>=10:

        new_word=""
        for lett in i:
            vals=dict[lett]*5+2
            if vals>25:
                vals=vals%26

            new_word+=dict_keys[dict_val[vals]]
        # print(new_word)

deszyfr= open("probka.txt","r").readlines()
tab= []
for i in deszyfr:
    tab.append(i.rstrip().split(" "))
# print(tab)


def szyfr(litera, a, b):
    vals = dict[litera] * a +b
    if vals > 25:
        vals = vals % 26
    return vals


for wyrazy in tab:
        for a in range(0,26):
            for b in range(0,26):
                punkty=0
                for numer_litera in range(0,len(wyrazy[0])):

                    if szyfr(wyrazy[0][numer_litera],a,b) == dict[wyrazy[1][numer_litera]]:
                        punkty+=1
                if punkty == len(wyrazy[0]):
                    punkty=0
                    print("szyfr",a,b)
        print(wyrazy)

for wyrazy in tab:
    wyrazy=list(reversed(wyrazy))
    for a in range(0, 26):
        for b in range(0, 26):
            punkty = 0
            for numer_litera in range(0, len(wyrazy[0])):

                if szyfr(wyrazy[0][numer_litera], a, b) == dict[wyrazy[1][numer_litera]]:
                    punkty += 1
            if punkty == len(wyrazy[0]):
                punkty = 0
                print("deszyfr", a, b)
    print(wyrazy)


