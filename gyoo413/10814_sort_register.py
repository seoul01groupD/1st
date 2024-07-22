n = int(input())
lst = []
for i in range(n):
    lst.append(list(input().split()))

for i in range(n):
    lst[i][0] = int(lst[i][0])
        

def merge_sorting(unsorted_list):

    length = len(unsorted_list)

    if length <= 1:
        return unsorted_list

    mid = length // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left = merge_sorting(left)
    right = merge_sorting(right)

    i, j = 0, 0
    sorted_list = []
    l = length // 2; r = (length + 1) // 2

    while(i < l and j < r):
        if left[i][0] <= right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while(i < l):
        sorted_list.append(left[i])
        i += 1
    while(j < r):
        sorted_list.append(right[j])
        j += 1

    return sorted_list
    


lst = merge_sorting(lst)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end = ' ')
    print('')