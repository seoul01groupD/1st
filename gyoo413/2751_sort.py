import sys

n = int(sys.stdin.readline())
num_list = []
for i in range(n):
    num_list.append(int(sys.stdin.readline()))


def merge_sort(lst):

    length = len(lst)

    if length <= 1:
        return lst
    
    mid = length // 2
    left = lst[:mid]
    right = lst[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    i = j = 0
    sorted_list = []
    l = length // 2; r = (length // 2) + 1

    while i < l and j < r:
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
        
    while i < l:
        sorted_list.append(left[i])
        i += 1

    while j < r:
        sorted_list.append(right[j])
        j += 1

    return sorted_list

num_list = merge_sort(num_list)

for num in num_list:
    print(num)