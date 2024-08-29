a=input("請輸入第 1 個點的 x, y 座標:")
x1,y1= map(int,a.split(','))
b=input("請輸入第 2 個點的 x, y 座標:")
x2,y2= map(int,b.split(','))
dist=((x1-x2)**2+(y1-y2)**2)**0.5
print(f"兩點的距離是:{dist:.2f}")
