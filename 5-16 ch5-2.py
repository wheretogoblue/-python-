a,b,c = map(int,input("請輸入3個整數值：").split(','))
sorted_numbers= sorted([a,b,c],reverse=True)
print("大到小分別是 ",sorted_numbers)
