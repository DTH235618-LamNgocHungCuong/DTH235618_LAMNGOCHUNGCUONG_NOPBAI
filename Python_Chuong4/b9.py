from math import sqrt

print ("Chương trình tính căn bậc 2 lồng nhau.")
n = int(input ("Nhập số dấu căn: "))
kq = 2

if n < 0:
    n = int(input ("Số không hợp lệ, yêu cầu nhập lại: "))

if n == 0:
    print ("Kết quả = ",kq)
elif n == 1:
    kq = sqrt(kq)
    print("Kết quả = ", kq)
else :
    kq = sqrt(kq)
    for i in range (1, n):
        kq = sqrt (kq + 2)
    print("Kết quả = ", kq)


