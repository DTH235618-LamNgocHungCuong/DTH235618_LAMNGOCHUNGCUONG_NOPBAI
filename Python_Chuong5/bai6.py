import re

c = input ("Nhập 1 chuỗi: ")
so = re.findall(r'-?\d+',c)
soam = re.findall(r'-\d+',c)

print (so)
print (soam)



