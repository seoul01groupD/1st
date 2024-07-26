num = int(input())
one_list = [0] * (num + 1)
index = 1

while index <= num:
    try:
        if one_list[index + 1] == 0 or one_list[index + 1] > one_list[index] + 1:
            one_list[index + 1] = one_list[index] + 1

        if one_list[2 * index] == 0 or one_list[2 * index] > one_list[index] + 1:
            one_list[2 * index] = one_list[index] + 1

        if one_list[3 * index] == 0 or one_list[3 * index] > one_list[index] + 1:
            one_list[3 * index] = one_list[index] + 1
        
        index += 1

    except:
        index += 1

print(one_list[num])
    