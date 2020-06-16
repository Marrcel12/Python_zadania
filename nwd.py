a=int(input("liczba1"))
b=int(input("liczba2"))
while(a!=b):
    if(a>b):
         a=a-b
    else:
         b=b-a
print(a)