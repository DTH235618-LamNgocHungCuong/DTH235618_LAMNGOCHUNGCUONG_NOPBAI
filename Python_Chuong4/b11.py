def sum1 (n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s

def sum2 ():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s

def sum3 ():
    s = 0
    for i in range(val, 0, -1):
        s += i
    return s

def main_1 ():
    global val
    val = 5
    print (sum1(5))
    print (sum2())
    print (sum3())

def main_2 ():
    global val
    val = 5
    print(sum1(5))
    print(sum3())
    print(sum2())

def main_3 ():
    global val
    val = 5
    print(sum2())
    print(sum1(5))
    print(sum3())

while True:
    n = int(input ("Chọn 1 trong 3 trường hợp (1),(2),(3) xảy ra, nhập số khác nếu không muốn tiếp tục: "))
    if n == 1:
        print("Trường hợp 1:")
        main_1()
    elif n == 2:
        print("Trường hợp 2:")
        main_2()
    elif n == 3:
        print("Trường hợp 3:")
        main_3()
    else:
        break

#Trường hợp 1 :  "5" "5"  "0"
#Trường hợp 2 :  "5" "15" "5"
#Trường hợp 3 :  "5" "5"  "0"
