high= (30,28,29,31,33,35,32)
low= (20,21,19,22,23,24,20)
print("過去一周的最高溫度",max(high))
print("過去一周的最低溫度",min(low))
averages= [(sum(t)/2) for t in zip(high,low)]
averages_str=' '.join(map(str, averages))
print("過去一周的平均溫度",averages_str)
