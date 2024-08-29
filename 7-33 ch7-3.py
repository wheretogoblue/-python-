money=int(input("請輸入存款本金："))
rate=float(input("請輸入年利率："))
y=int(input("請輸入多少年："))
for i in range(y):
    money *= (1+rate)
    print("第 %d年本金和： %d"%((i+1),int(money)))

