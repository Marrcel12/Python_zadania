def fibb(a):
    if a == 0:
        return 0
    elif a==1:
        return 1
    else:
        return fibb(a-1)+fibb(a-2)

print(fibb(1))
