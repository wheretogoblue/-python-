import math
a,b=map(int,input("請輸入點座標：").split(','))
r=20
dist=math.sqrt(a**2+b**2)
if dist>r:
    print(f"點座標({a},{b})不在圓內部")
else:
    print(f"點座標({a},{b})在圓內部")
