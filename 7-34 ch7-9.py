import math
results= []
for i in range(10,101,10):
    e_value= sum(1/math.factorial(k) for k in range(i+1))
    results.append((i, e_value))
for i, value in results:
    print("當i是 %3d 時 e= %.39f" %(i,value))
