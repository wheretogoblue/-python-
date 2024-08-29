A= {n for n in range(1,100,2)}
primes=[]
for num in range(2,101):
    is_prime= True
    for i in range(2, int(num** 0.5)+1):
        if num % i == 0:
            is_prime= False
            break
    if is_prime:
         primes.append(num)
B= set(primes)

a1= A | B
a2= A & B
a3= A - B
a4= B - A
a5= a1-a2

print("聯集：",a1)
print("交集：",a2)
print("A-B差集：",a3)
print("B-A差集：",a4)
print("AB對稱差集：",a5)

