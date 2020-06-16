from decimal import Decimal
plik= open("funkcje.txt","r").readlines()

dane=[]
for i in plik:
    dane.append(i.rstrip().split("\t"))

# print(dane)
def fy(x):
       f=0
       if x >=0  and x<1:
          f=0
       elif x >= 1 and x < 2:
           f=1
       elif x >=2 and x < 3:
           f=2
       elif x >= 3 and x < 4:
           f = 3
       elif x >= 4 and x < 5:
           f = 4

       return float(dane[f][0]) + float(dane[f][1])*float(x) + float(dane[f][2])*float(x**2) + float(dane[f][3])*float(x**3)
print(round(fy(1.5),5))
max=2.0
i=0.0
x_max=0
while i< 5:
    if max < fy(i):
        max = fy(i)
        x_max=i
    i+=0.001
print(round(x_max,4),max)
i=0.0

def bisekcja(a, b):
    c = a
    while ((b - a) >= 0.0001):

        c = (a + b) / 2.0

        if (fy(c) == 0.0):
            break

        if (fy(c) * fy(a) < 0):
            b = c
        else:
            a = c
    return c
a = 0
b = 0.99999
print(round(bisekcja(a, b),5))

a=2.0
b = 2.99999
print(round(bisekcja(a, b),5))

a=3.0
b = 3.99999
print(round(bisekcja(a, b),5))

a=4.0
b = 4.99999
print(round(bisekcja(a, b),5))