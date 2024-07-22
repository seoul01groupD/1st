import sys

input = sys.stdin.readline
T = int(input())

for test in range(T):
    k = int(input())
    n = int(input())

    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    ans = int(factorial(n + k) / (factorial(n - 1) * factorial(k + 1)))
    print(ans)