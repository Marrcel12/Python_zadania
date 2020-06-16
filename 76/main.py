file = open("szyfr1.txt", "r").readlines()
tab = []
for i in file:
    tab.append(i.rstrip())

# print(tab)
temp_key = tab[6].split(" ")
key = []
for i in temp_key:
    key.append(int(i))
tab = tab[0:6]
# print(key, tab)
for wyraz in tab:
    wyraz = list(wyraz)
    for pozycja in range(0, 50):
        temp = wyraz[pozycja]
        wyraz[pozycja] = wyraz[key[pozycja] - 1]
        wyraz[key[pozycja] - 1] = temp
    # print("".join(wyraz))

# zad2
file2 = open("szyfr2.txt", "r").readlines()
tab2 = []
for i in file2:
    tab2.append(i.rstrip())
temp_key = tab2[1].split(" ")
key = []
for i in temp_key:
    key.append(int(i))
tab2 = tab2[:1]
# print(tab2, key)
i = 0
old_key = key
while len(tab2[0]) != len(key):
    if (i > len(old_key) - 1):
        i = 0
    key.append(old_key[i])
    i += 1
# print(key)
for wyraz in tab2:
    wyraz = list(wyraz)
    for i in range(0, 50):
        temp = wyraz[i]
        wyraz[i] = wyraz[key[i] - 1]
        wyraz[key[i] - 1] = temp
    # print("".join(wyraz))

# zad3
wyraz3 = open("szyfr3.txt", "r").read().rstrip()
key = [6, 2, 4, 1, 5, 3]
i = 0
old_key = key
while len(tab2[0]) != len(key):
    if (i > len(old_key) - 1):
        i = 0
    key.append(old_key[i])
    i += 1
# czemu nie dziaalo z reversowana tablica?

for i in range(49, -1, -1):
    wyraz3 = list(wyraz3)
    temp = wyraz3[i]
    wyraz3[i] = wyraz3[key[i] - 1]
    wyraz3[key[i] - 1] = temp

print("".join(wyraz3))
