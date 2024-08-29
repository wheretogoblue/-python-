import math
n=int(input("請輸入正多邊形邊數"))
s=float(input("請輸入正多邊形邊長"))
area=(n*s**2)/(4*math.tan(math.pi/n))
print("area=",area)
