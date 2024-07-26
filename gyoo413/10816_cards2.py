import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_dict = {}
for e in n_list:
    n_dict[str(e)] = n_dict.get(str(e), 0) + 1

for e in m_list:
    print(n_dict.get(str(e), 0), end = ' ')