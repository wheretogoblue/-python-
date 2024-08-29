dist=384400
speed=int(input("請輸入火箭速度馬赫數："))*1225
total_hours=dist // speed
days= total_hours // 24
hours= total_hours % 24
print("總共需要%d天,%d小時"%(days,hours))
