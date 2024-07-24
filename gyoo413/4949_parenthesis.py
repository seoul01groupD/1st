def word_stack(lst):

    my_stack = []
    index = 0

    while index < len(lst):

        if lst[index] == '(' or lst[index] == '[':
            my_stack.append(lst[index])

        elif lst[index] == ')':
            if len(my_stack) == 0:
                return 'no'
            elif my_stack[-1] == '(':
                my_stack.pop()
            else:
                return 'no'
            
        elif lst[index] == ']':
            if len(my_stack) == 0:
                return 'no'
            elif my_stack[-1] == '[':
                my_stack.pop()
            else:
                return 'no'

        index += 1

    return 'yes'

while True:
    s = list(input())

    sentence = []
    for word in s:
        sentence.extend(word)

    if s == ['.']:
        break

    else:
        print(word_stack(sentence))
