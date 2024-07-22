n = int(input())

ans_lst = []
num = 1

while(len(ans_lst) <= n):
    if '666' in str(num):
        ans_lst.append(num)
    num += 1
    
print(ans_lst[n-1])