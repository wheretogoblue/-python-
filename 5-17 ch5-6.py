h=int(input("請輸入本週工作時數："))
m=150
if h<40:
    pay=m*0.8*h
elif h==40:
    pay=m*h
elif 40<h<=50:
    pay=m*1.2*h
else :
    pay=m*1.6*h
print(f"本週薪資{pay:.0f}")
