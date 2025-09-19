def tong_uoc(n):
    tong = 0
    for i in range(1,n):
        if n % i == 0:
            tong += i
    return tong

def kt_shthien(n):
    return tong_uoc(n) == n

def kt_stvuong(n):
    return tong_uoc(n) > n

n = int(input ("Nhập số nguyên dương n: "))

print (f"Số {n} là số hoàn thiện? {kt_shthien(n)}")
print (f"Số {n} là số thịnh vượng? {kt_stvuong(n)}")
