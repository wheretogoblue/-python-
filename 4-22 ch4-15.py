a,v =map(float,input("請輸入加速度 a 和速度 v ：").split(','))
d=v**2/(2*a)
print(f"所需跑道長度 {d:.1f}公尺")
