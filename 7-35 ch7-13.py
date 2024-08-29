def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
primes = []
num = 2 #從2開始檢查
while len(primes) < 20:
    if is_prime(num):
        primes.append(num)
    num += 1

print(primes)
