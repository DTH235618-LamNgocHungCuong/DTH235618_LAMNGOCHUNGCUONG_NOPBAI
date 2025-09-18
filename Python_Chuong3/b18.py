for i in range(4):
    if (i==0) or (i==3):
        print(' * ' * 4)
    else:
        print(' * ' + ' ' * 6+ ' * ')

print ()
for i in range(4):
    print('   ' * (3-i) + ' * ' * (i+1))

print ()
for i in range(7):
    if (i==0) or (i==6):
        print('   ' * i + ' * ')
    elif (i==1) or (i==5):
        if (i<3):
            i=0
        print('   ' * i +' * ' * 2)
    elif (i==2) or (i==4):
        if (i<3):
            i=0
        print('   ' * i + ' * ' + ' ' * 3 + ' * ')
    else:
        print(' * ' * 7)