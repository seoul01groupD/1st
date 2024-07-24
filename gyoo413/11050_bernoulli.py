n, k = map(int, input().split())

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
c_combination_k = int(factorial(n) / (factorial(n - k) * factorial(k)))

print(c_combination_k)