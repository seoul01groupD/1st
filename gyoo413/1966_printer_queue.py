t = int(input())

for i in range(t):
    n, target = map(int, input().split())
    my_queue = list(map(int, input().split()))
    importance = sorted(my_queue)
    output_list = []

    while my_queue[target] != importance[-1] or target != 0:

        if my_queue[0] == importance[-1]:
            my_queue.pop(0)
            output_list.append(importance.pop())
        else:
            my_queue.append(my_queue.pop(0))

        if target == 0:
            target = len(my_queue) - 1
        else:
            target -= 1

    print(len(output_list) + 1)