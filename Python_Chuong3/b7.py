from datetime import datetime, timedelta

ngay = int(input ("Nhập ngày: "))
thang = int(input ("Nhập tháng: "))
nam = int(input ("Nhập năm: "))

try:
    # Tạo đối tượng ngày
    d = datetime (nam, thang, ngay)
    # Tìm ngày kế tiếp
    ngaykt = d + timedelta(days = 1)
    print ("Ngày kế tiếp là: {}/{}/{}".format(ngaykt.day, ngaykt.month, ngaykt.year))
except ValueError:
    print ("Ngày không hợp lệ")