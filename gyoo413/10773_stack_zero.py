import sys
input = sys.stdin.readline

n = int(input())

my_stack = []
for i in range(n):
    num = input().rstrip()

    if num != '0':
        my_stack.append(int(num))
    else:
        if len(my_stack) == 0:
            continue
        else:
            my_stack.pop()

print(sum(my_stack))
