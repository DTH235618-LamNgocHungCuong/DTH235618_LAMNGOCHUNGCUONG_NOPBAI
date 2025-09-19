
month = int(input ("Nhập vào 1 tháng (1-12): "))

if 1 <= month <= 3:
    print ("Tháng ", month, "thuộc quý 1")
elif 4 <= month <= 6:
    print ("Tháng ", month, "thuộc quý 2")
elif 7 <= month <= 9:
    print ("Tháng ", month, "thuộc quý 3")
elif 10 <= month <= 12:
    print ("Tháng ", month, "thuộc quý 4")
else:
    print("Tháng không hợp lệ.")