week= {'Monday':'星期一',
       'Tuesday':'星期二',
       'Wednesday':'星期三',
       'Thursday':'星期四',
       'Friday':'星期五',
       'Saturday':'星期六',
       'Sunday':'星期日'}
a=input("請輸入星期幾的英文：").capitalize()
if a in week:
    print(week[a])
else:
    print("輸入錯誤")
