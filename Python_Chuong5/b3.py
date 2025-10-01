def CheckPrime (x):
    dem = 0
    for i in range(1, x + 1):
        if x % i == 0:
            dem += 1
    return dem == 2 #trả về nếu đếm = 2
chon = input ("Nhấn s để lấy chuỗi trong đề bài, nhấn ngẫu nhiên để nhập chuỗi: ")
if chon == "s":
    s = "5;7;8;-2;8;11;-13;9;10"
else:
    s = input ("Nhập chuỗi số: ")

arr = s.split(";")
sochan = 0
soam = 0
sont = 0
sum = 0
for x in arr:
    print (x)
    number = int (x)
    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        sont += 1
    sum += number
print ("Số chẵn = ", sochan)
print ("Số âm = ", soam)
print ("Số Nguyên tố = ", sont)
print ("Trung bình = ", sum/len(arr))