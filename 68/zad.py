file= open("dane_napisy.txt").readlines()
tab=[]
# jednolite=0
# anagram_zaw=0
for i in range(0,1000):

    tab.append(file[i].rstrip().split(' '))
# for i in tab:
#     if i[0]==i[1] and i[0][0]==i[0][1]:
#         jednolite+=1
# for i in tab:
#     if sorted(i[0])== sorted(i[1]):
#         anagram_zaw+=1
# # print(anagram_zaw)
najwiecej=0
slowo=""
for i in range(0,1000):
    anagramy=0
    for j in range(i,1000):
        if sorted(tab[i][0]) == sorted(tab[j][0]):
            anagramy+=1
        if sorted(tab[i][0]) == sorted(tab[j][1]):
            anagramy+=1
    if anagramy>najwiecej:
        najwiecej=anagramy
        slowo=tab[i][0]
    if anagramy > najwiecej:
        najwiecej = anagramy


print(najwiecej)
