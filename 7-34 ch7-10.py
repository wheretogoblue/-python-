nums=list(range(1,10))
for i in range(len(nums)):
    for j in range(len(nums) - i):
        print(nums[j],end ="")
    print()
