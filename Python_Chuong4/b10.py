import time

for i in range(7):
    if (i==0) or (i==1) or (i==2):
        print ("   " * 3 + " * " * (i+1))
    elif (i==4) or (i==5) or (i==6):
        print (" * " * (7-i))
    else:
        print (" * " * 7)

print()
time.sleep(1)

for i in range(7):
    if (i==0) or (i==1) :
        print ("   " * 3 + " * " * (i+1))
    elif (i==2):
        print("   " * 3 + " *     * ")
    elif (i==4):
        print(" *     * ")
    elif (i==5) or (i==6):
        print (" * " * (7-i))
    else:
        print (" * " * 7)

print()
time.sleep(1)

for i in range(3):
    print ("   " * 3 + " * " * (4-i))
for i in range(4):
    print ("   " * (3-i) + " * " * (i+1))

print()
time.sleep(1)

for i in range(3):
    if (i==1):
        print("   " * 3 + " *     * ")
    else :
        print ("   " * 3 + " * " * (4-i))
for i in range(4):
    if (i==2):
        print("   " * (3-i) + " *     * ")
    else :
        print ("   " * (3-i) + " * " * (i+1))
