input_score=input("請輸入5個考試成績：")
score=[int(x) for x in input_score.split(',')]
print("分數串列      ：",score)
score.sort(reverse=True)
print("高分往低分排列：",score)
score.sort()
print("低分往高分排列：",score) 
print("最高分    ：",max(score))
print("總分      ：",sum(score))
