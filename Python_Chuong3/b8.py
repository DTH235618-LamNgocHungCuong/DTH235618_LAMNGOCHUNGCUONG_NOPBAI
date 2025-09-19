
a = float(input ("Nhập số a: "))
b = float(input ("Nhập số b: "))
pt = input ("Nhập 1 trong các phép toán (+,-,*,/): ")

if pt == "+":
    print (f"Kết quả phép toán: {a + b}")
elif pt == "-":
    print (f"Kết quả phép toán: {a - b}")
elif pt == "*":
    print (f"Kết quả phép toán: {a * b}")
elif pt == "/":
    if b != 0:
        print (f"Kết quả phép toán: {a / b}")
    else:
        print ("Lỗi: Không thể chia hết cho 0!")
else:
    print("Lỗi: Phép toán không hợp lệ!")