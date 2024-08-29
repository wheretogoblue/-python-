import math

r=6371
x1, y1= map(float,input("請輸入第一個地點的經緯度:").split(','))
x2, y2= map(float,input("請輸入第二個地點的經緯度:").split(','))
distance= r*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+
                      math.cos(math.radians(x1))*math.cos(math.radians(x2))*
                      math.cos(math.radians(y1-y2)))
print("distance=",distance)
