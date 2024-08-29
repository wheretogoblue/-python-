answer = 30
guess = 0
attempts = 0
while guess != answer:
    guess = int(input("請猜1-100間的數字 = "))
    attempts += 1
    if guess > answer:
        print("請猜小一點")
    elif guess < answer:
        print("請猜大一點")
    else:
        print("恭喜答對了")
        print(f"共猜了{attempts}次")
