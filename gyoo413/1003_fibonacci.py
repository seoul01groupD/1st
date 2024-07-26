fibo_list = []

def fibonacci(n):
    
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]
    else:
        return [fibo_list[n - 1][0] + fibo_list[n - 2][0], fibo_list[n - 1][1] + fibo_list[n - 2][1]]

for f in range(41):
    fibo_list.append(fibonacci(f))


t = int(input())

for i in range(t):
    num = int(input())
    print(fibo_list[num][0], end = ' ')
    print(fibo_list[num][1])
