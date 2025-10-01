def CheckDoiXung (s):
    flag = True
    for i in range (len (s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag
def main ():
    print ("Nhập 1 chuỗi: ")
    c = input ()
    if CheckDoiXung (c):
        print ("Chuỗi nhập đối xứng.")
    else:
        print ("Chuỗi nhập không đối xứng.")
while True:
    main()
    print ("Tiếp tục?(c/k): ")
    tl = input ()
    if tl == "k":
        break
print ("Cảm ơn.")