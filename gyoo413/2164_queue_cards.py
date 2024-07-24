import math

n = int(input())

k = int(math.log(n, 2))
if n - (2 ** k) != 0:
    ans = (n - (2 ** k)) * 2
else:
    ans = n

print(ans)