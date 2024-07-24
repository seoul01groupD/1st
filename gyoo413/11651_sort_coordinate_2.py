import sys

input = sys.stdin.readline
n = int(input())
coordinate = []
for i in range(n):
    coordinate.append(list(map(int, input().split())))

ans = sorted(coordinate, key = lambda coordinate: [coordinate[1], coordinate[0]])

for i in ans:
    for j in range(2):
        print(i[j], end = ' ')
    print('')