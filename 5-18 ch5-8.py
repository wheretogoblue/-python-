a,b,c =map(int,input("請輸入3邊長：").split(','))
d= a+b+c
if a+b>c and a+c>b and b+c>a:
    print(f"三角形周長是{d}")
else:
    print("這不是三角形的邊長")
