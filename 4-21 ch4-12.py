x1,y1= map(float,input("請輸入第 1 個點的 x, y 座標:").split(','))
x2,y2= map(float,input("請輸入第 2 個點的 x, y 座標:").split(','))
x3,y3= map(float,input("請輸入第 3 個點的 x, y 座標:").split(','))
dist1=((x1-x2)**2+(y1-y2)**2)**0.5
dist2=((x2-x3)**2+(y2-y3)**2)**0.5
dist3=((x3-x1)**2+(y3-y1)**2)**0.5
p=(dist1+dist2+dist3)/2
area= (p*(p-dist1)*(p-dist2)*(p-dist3))**0.5
print(f"三角形的面積是:{area:.2f}")
