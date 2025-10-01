def ToiUuChuoi (s):
    s2 = s
    s2 = s2.strip()
    arr = s2.split(' ')
    s2=""
    for i in arr:
        word = i
        if len(word.strip()) != 0:
            s2 += word + " "
    return s2.strip()

s = "     Trần    Duy     Thanh   "
print (s, "=>", len(s))
s = ToiUuChuoi(s)
print (s, "=>", len(s))

c = input ("Nhập chuỗi: ")
print (c, "=>", len(c))
c = ToiUuChuoi(c)
print (c, "=>", len(c))