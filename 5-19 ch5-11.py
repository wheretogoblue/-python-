a,b,c,d,e,f=map(int,input("請輸入線性方程式的係數：").split(','))
if a*d-b*c==0:
    print("此線性方程式沒有解答")
else:
    x=(e*d-b*f)/(a*d-b*c)
    y=(a*f-e*c)/(a*d-b*c)
    print("x= %6.4f, y= %6.4f"%(x,y))
