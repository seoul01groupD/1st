n = int(input())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
s = list(str(factorial(n)))

cnt = 0

while s[-1] == '0':
    s.pop()
    cnt += 1

print(cnt)