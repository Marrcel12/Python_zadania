def f(x):
    return pow(x,4)/500-pow(x,2)/200 - 3/250
def g(x):
    return -1*(-1*pow(x,3)/30 +x/20+1/6)

x =2
poleF=0
poleG=0
szac=1/1000
while x<10:
    poleF+=(f(x)+f(x+szac)) * szac/2
    poleG+=(g(x)+g(x+szac)) * szac/2
    x+=1/1000
print(poleF+poleG)
