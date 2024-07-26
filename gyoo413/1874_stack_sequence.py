import sys
input = sys.stdin.readline

n = int(input())
sequence = []
for i in range(n):
    sequence.append(int(input()))

my_stack = []
push_list = [x + 1 for x in range(n + 1)][::-1]
output_list = []
ans = []
flag = 0

for num in sequence:
    if num >= push_list[-1]:
        while num != push_list[-1]:
            my_stack.append(push_list.pop())
            ans.append('+')
        output_list.append(push_list.pop())
        ans.append('+')
        ans.append('-')
    elif num == my_stack[-1]:
        output_list.append(my_stack.pop())
        ans.append('-')
    else:
        print('NO')
        flag += 1
        break

if flag == 0:
    for op in ans:
        print(op)
