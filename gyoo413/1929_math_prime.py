m, n = map(int, input().split())

def find_prime(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    else:
        return True
    

for i in range(m, n + 1):
    if find_prime(i):
        print(i)
