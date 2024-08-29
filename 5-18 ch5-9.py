height=input("請輸入身高(公分)：")
weight=input("請輸入體重(公斤)：")
bmi= int(weight)/((float(height)/100)**2)
if 18.5<=bmi<24:
    print("正常")
elif bmi<18.5:
    print("體重過輕")
elif 24<=bmi<27:
    print("超重")
else:
    print("肥胖")
