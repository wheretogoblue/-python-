nums=list(range(9,0, -1))
for i in range(len(nums)):
    spaces= 9- (i+1)
    print(" "* spaces, end="")
    for j in range(i+1):
        print(nums[j],end ="")
    print()
