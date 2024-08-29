print("猜數字遊戲，請心中想一個 0 - 7 之間的數字，然後回答問題")

# 問題1
print("第一個問題：你心中的數字是否在以下集合中？")
print("1, 3, 5, 7")
a = input("輸入y或Y代表有，其他代表無：")

# 問題2
print("第二個問題：你心中的數字是否在以下集合中？")
print("2, 3, 6, 7")
b = input("輸入y或Y代表有，其他代表無：")

# 問題3
print("第三個問題：你心中的數字是否在以下集合中？")
print("4, 5, 6, 7")
c = input("輸入y或Y代表有，其他代表無：")

# 根據回答確定用戶心中的數字
number = 0
if a == 'y' or a == 'Y':
    number += 1
if b == 'y' or b == 'Y':
    number += 2
if c == 'y' or c == 'Y':
    number += 4

print(f"讀者心中所想的數字是：{number}")
