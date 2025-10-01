def ToiUuChuoi(s):
    s2=s
    s2=s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word=x
        if len(word.strip())!=0:
            tu = word.capitalize()
            print(tu)
            s2=s2+tu+" "
    return s2.strip()



s="  TRần  duY      thAnH "
print(s)
s=ToiUuChuoi(s)
print(s)


