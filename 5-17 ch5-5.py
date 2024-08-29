print("""
溫度轉換選擇
1:華氏溫度轉成攝氏溫度
2:攝氏溫度轉華氏溫度""")
a=int(input("=")) #1或2
if a==1:
    f=int(input("請輸入華氏溫度："))
    c=(f-32)/9*5
    print(f"華氏溫度 {f}等於攝氏溫度 {c}")
elif a==2:
    c=int(input("請輸入攝氏溫度："))
    f=c*9/5+32
    print(f"攝氏溫度 {c}等於華氏溫度 {f}")
    
else:
    print("輸入錯誤")
