plik=open("anagram.txt")
tab=[]
for line in plik:
    tab.append(line.replace('\n', '').split())
to_save=[]
for line in tab:
    lenght= len(line[0])
    local_counter=0
    for word in line:
        if lenght == len(word):
            local_counter+=1
    if local_counter==5:
        to_save.append(line)
save=open('odp_4a.txt','w')

for i in to_save:
    for j in i:
        save.write(j+" ")
    save.write("\n")
# zad 2


save=open('odp_4b.txt','w')
for line in tab:
    count=0
    first_one=sorted(line[0])
    for word in line:
        if sorted(word)==first_one:
            count+=1
    if count==5:
        for i in line:
            save.write(i+" ")
        save.write("\n")

















