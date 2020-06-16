def fib(fn):
    last=1
    pre_last=1
    if fn==1 or fn==2:
        return 1
    for i in range(0, fn-2):
        temp=last
        last+=pre_last
        pre_last=temp

    return last
def pierwsza(a):
    if a ==1:
        return False
    for z in range(2, a):
        if a % z == 0:
            return False
    return True

# print(fib(10))
# print(fib(20))
# print(fib(30))
# print(fib(40))
# print("\n")
# for i in range(1, 41):
#     if pierwsza(fib(i)):
#         print(fib(i))
# print("\n")
len_max=len(str(bin(fib(40)).replace("0b","")))-1
rep_binarna=""
fraktal_40=""
for i in range(1,40):
    line=str(bin(fib(i)).replace("0b",""))
    rep_binarna+=str(bin(fib(i)).replace("0b",""))+"\n"
    while len(line)!=len_max:
        line="0"+line
    # print(line)


# print(rep_binarna)

for i in range(1,40):
    liczba=0
    for z in bin(fib(i)).replace("0b",""):
        if z =="1":
            liczba+=1
    if liczba==6:
        print(bin(fib(i)).replace("0b",""))

