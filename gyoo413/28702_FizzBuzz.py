s = []
for i in range(3):
    s.append(input())

def reverse_fizzbuzz(lst):
    for s in lst:
        try:
            return [int(s), lst.index(s)]
        except:
            continue

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else: 
        return str(x)
    
ans = 0

if reverse_fizzbuzz(s)[1] == 0:
    ans = reverse_fizzbuzz(s)[0] + 3
elif reverse_fizzbuzz(s)[1] == 1:
    ans = reverse_fizzbuzz(s)[0] + 2
elif reverse_fizzbuzz(s)[1] == 2:
    ans = reverse_fizzbuzz(s)[0] + 1

ans = fizzbuzz(ans)

print(ans)
