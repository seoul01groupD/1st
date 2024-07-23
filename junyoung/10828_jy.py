import sys
input=sys.stdin.readline
n=int(input())
c=[]
for i in range(n):
    m=list(input().split())
    match m[0]:
        case "push":
            c.append(m[1])
        case "pop":
            if len(c)==0:
                print(-1)
            else:
                print(c[-1])
                c.pop()
        case "size":
            print(len(c))
        case "empty":
            if len(c)==0:
                print(1)
            else:
                print(0)
        case "top":
            if len(c)==0:
                print(-1)
            else:
                print(c[-1])
## match case 구문이라 못 씀... 궁금하면 검색해 보세요.