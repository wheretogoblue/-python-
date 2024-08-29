days= ["星期天","星期一","星期二","星期三","星期四","星期五","星期六"]
print("今天星期日")
a=int(input("請輸入天數："))
b=(0+a)%7
b_days=days[b]
print(f"{a}天後是{b_days}")
