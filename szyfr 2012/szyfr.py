to_cryp=open("tj.txt","r").read().split("\n")
key= open("klucze1.txt","r").read().split("\n")
key_cryp={}
result=open("wynik4a.txt","w+")
alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

for i in range(0,120):
    key_cryp[key[i]]=to_cryp[i]

for combination in key_cryp:
    word =key_cryp[combination]
    key = combination
    if(len(word)>len(key)):
        key+=key*(len(word)-len(key))
    word_to_save=""
    for i in range(0,len(word)):
        new=ord(word[i])+alphabet.find(key[i])+1
        if(new > 90):
            new-=26
        word_to_save+=chr(new)
    result.write(word_to_save+"\n")
# b
to_encryp=open("sz.txt","r").read().split("\n")
key= open("klucze2.txt","r").read().split("\n")
result=open("wynik4b.txt","w+")
key_encryp={}
for i in range(0,120):
    key_encryp[key[i]]=to_encryp[i]

for combination in  key_encryp:
    word = key_encryp[combination]
    key = combination
    word_to_save = ""
    if (len(word) > len(key)):
        key += key * (len(word) - len(key))
    for i in range(0, len(word)):
        new = ord(word[i]) - (alphabet.find(key[i]) + 1)
        if (new < 65 ):
            new += 26
        print(new)
        word_to_save += chr(new)
    result.write(word_to_save + "\n")