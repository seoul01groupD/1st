import sys

input = sys.stdin.readline
k, n = map(int, input().split())
line = []
for i in range(k):
    line.append(int(input()))

m = max(line)
start = 1; end = m

if n == 1:
    print(m)
else:
    while start <= end:
        cnt = 0
        mid = (start + end) // 2

        for i in line:
            cnt += (i // mid)

        if cnt >= n:
            start = mid + 1
        else:
            end = mid - 1
            
    print(end)