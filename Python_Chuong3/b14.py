a = 0
c = 0
while a < 100:
    b = 0
    while b < 40:
        if (a+b) % 2 == 0:
            print('*', end=' ')
            c += 1
        b += 1
    print()
    a += 1
print (c)

#2000 dấu *