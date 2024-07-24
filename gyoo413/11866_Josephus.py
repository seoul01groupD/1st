n, k = map(int, input().split())

my_queue = [(x + 1) for x in range(n)]
counting_index = 0
output_list = ['<']

while len(output_list) < 2 * n + 1:
    if (counting_index + 1) % k == 0:
        output_list.append(str(my_queue.pop(0)))
        output_list.append(', ')
    else:
        my_queue.append(my_queue.pop(0))

    counting_index += 1

output_list.pop()
output_list.append('>')
print(''.join(output_list))