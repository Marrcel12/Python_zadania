def bin_dec(bin):
    dec=0
    power=0
    while bin > 0 :
        dec += 2 ** power*(bin % 10)
        bin //= 10
        power += 1
    return dec

print(bin_dec(10111))

print(bin(23))
print(int(bin(23),2))