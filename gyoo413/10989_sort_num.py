import sys

input = sys.stdin.readline
n = int(input())
unsorted_list = [0] * 10000

for i in range(n):
    unsorted_list[int(input()) - 1] += 1

for i in range(len(unsorted_list)):
    for j in range(unsorted_list[i]):
        print(i + 1)