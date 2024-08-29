a,b,c=map(int,input("請輸入一元二次方程式的係數:").split(','))
d=b**2-4*a*c
if d>=0:
    r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    if d>0:
        print("有2個根")
        print("r1= %6.4f, r2= %6.4f"% (r1,r2))
    else:
        print("有1個根")
        print("r1= %6.4f"% r1)
else:
    print("沒有實數根")
