import math

def Tlog (x,a):
   return math.log (x)/math.log(a)

print ("Chương trình tính logax.")
x = int(input ("x = "))
a = int(input ("a = "))

logax = Tlog (x,a)
print ("logax = ",logax)

