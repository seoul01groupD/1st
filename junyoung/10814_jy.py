import sys
input=sys.stdin.readline
def my_len(list1):
    count=0
    for i in list1:
        count+=1
    return count
def sorting(list1):
    length=my_len(list1)
    if length==1:
        return list1
    else:
        i=0
        j=0
        count=0
        list2=sorting(list1[:length//2])
        list3=sorting(list1[length//2:])
        list4=[]
        while count<length:
            if i>=length//2:
                list4.append(list3[j])
                count+=1
                j+=1
            elif j>=(length+1)//2:
                list4.append(list2[i])
                count+=1
                i+=1
            else:
                count+=1
                if list2[i]>list3[j]:
                    list4.append(list3[j])
                    j+=1
                else:
                    list4.append(list2[i])
                    i+=1
        return list4
n=int(input())
users=[]
for i in range(n):
    age,name=input().split( )  
    age=int(age)
    users.append([age,i,name])
for i in sorted(users):
    print(i[0], i[2])