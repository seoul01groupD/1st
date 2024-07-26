t = int(input())

for i in range(t):
    s = list(input())

    def parenthesis(lst):
        my_stack = []
        index = 0

        while index < len(lst):
            if s[index] == '(':
                my_stack.append(lst[index])
            else:
                if len(my_stack) == 0:
                    return 'NO'
                elif my_stack[-1] == '(':
                    my_stack.pop()
                else:
                    return 'NO'
            
            index += 1

        if len(my_stack) == 0:
            return 'YES'
        else:
            return 'NO'
        
    print(parenthesis(s))
    
    