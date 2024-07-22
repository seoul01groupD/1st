n = int(input())

def comp_sum(integer):
    lst = [integer]
    for i in range(len(list(str(integer)))):
        lst.append(integer % 10)
        integer //= 10
    return(sum(lst))


for i in range(n):
    if comp_sum(i) == n:
        print(i)
        break
    elif i == (n - 1):
        print(0)