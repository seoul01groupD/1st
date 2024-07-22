n = int(input())

number = [1]
i = 0
while number[i] <= 1000000000:
    i += 1
    number.append(number[i-1] + (6 * i))

if n == 1:
    print(1)
else:
    for i in range(len(number)):
        if number[i-1] < n <= number[i]:
            print(i+1)
        else:
            continue