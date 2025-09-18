x = int(input ("Nhập x: "))
n = int(input ("Nhập n: "))

s = 0

for i in range(0, n + 1):
    tu = x**(2*i+1)
    mau = 1
    for j in range(1, 2 * i + 2):
        mau *= j
    print ("{0}, {1}",tu , mau)
    s = s + (tu/mau)
print ("s ({0}, {1}) = {2}".format(x, n, s) )