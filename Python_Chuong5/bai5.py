import re

def NguyenAm (c):
    return c.lower() in 'aeiou'

def PhuAm (c):
    return c.isalpha() and not NguyenAm(c)

def main ():
    demInHoa = 0
    demInThuong = 0
    demSo = 0
    demKTDB = 0
    demKTrang = 0
    demNAm = 0
    demPAm = 0
    c = input ("Nhập 1 chuỗi: ")

    for i in range (len (c)):
        if c[i].isupper():
            demInHoa += 1
        elif c[i].islower():
            demInThuong += 1
        elif c[i].isdigit():
            demSo += 1
        elif c[i].isspace():
            demKTrang += 1
        elif c[i].isalpha(): #kiểm tra chữ cái (loại bỏ ký tự đặc biệt)
            if NguyenAm(c[i]):
                demNAm += 1
            elif PhuAm(c[i]):
                demPAm += 1
        else:
            demKTDB +=1
    

    print ("Số chữ in hoa có trong chuỗi là: ", demInHoa)     
    print ("Số chữ in thường có trong chuỗi là: ", demInThuong) 
    print ("Số chữ số có trong chuỗi là: ", demSo) 
    print ("Số khoản trắng có trong chuỗi là: ", demKTrang)
    print ("Số nguyên âm có trong chuỗi là: ", demNAm)
    print ("Số phụ âm có trong chuỗi là: ", demPAm)
    print ("Số ký tự đặc biệt có trong chuỗi là: ", demKTDB)


while True:
    main()
    chon = input ("Nhấn k để dừng lại, nhấn các nut khác đễ tiếp tục: ")
    if chon == "k":
        break
print ("Cảm ơn đã tham gia.")    