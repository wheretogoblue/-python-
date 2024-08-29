print("9 * 9 Multiplication Table".center(30))
print(" ".join(str(x) for x in range(1,10)).center(30))
print("=" * 35)
for i in range(1,10):
    row = [f"{i * j:2}" for j in range(1,10)]
    print(f"{i} | "+" ".join(row))

      
      
