from math import sqrt
def TDo (xA,yA,xB,yB):
    return sqrt ((xB-xA)**2 + (yB-yA)**2)

print ("Chương trình tính tọa độ 2 điểm.")
print ("Nhập tọa độ điểm A(xA,yA)")
xA = int(input ("xA = "))
yA = int(input ("yA = "))
print("Nhập tọa độ điểm B(xB,yB)")
xB = int(input ("xB = "))
yB = int(input ("yB = "))
tdo = TDo (xA,yA,xB,yB)
print ("|AB| = dAB = ",tdo)