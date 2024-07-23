n,m=map(int,input().split())
chess=[0]*n
minimum=m*n
for i in range(n):
    chess[i]=list(input())
for i in range(n-7):
    for j in range(m-7):
        count=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if chess[k][l]=='B':
                        count=count+1
                else:
                    if chess[k][l]=='W':
                        count=count+1
        if count<minimum:
            minimum=count
for i in range(n-7):
    for j in range(m-7):
        count=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2==0:
                    if chess[k][l]=='W':
                        count=count+1
                else:
                    if chess[k][l]=='B':
                        count=count+1
        if count<minimum:
            minimum=count

print(minimum)            