import sys
input=sys.stdin.readline
n=int(input())
c=[]
d=n*0.15
if d-int(d)>=0.5:
    m=int(d)+1
else:
    m=int(d)
if n==0:
    print(0)
else:
    for i in range(n):
        c.append(int(input()))
    c=sorted(c)
    e=c[m:n-m]
    f=sum(e)/(n-2*m)
    if f-int(f)>=0.5:
        print(int(f)+1)
    else:
        print(int(f))
## 변수 이름이 알아보기 힘듦;