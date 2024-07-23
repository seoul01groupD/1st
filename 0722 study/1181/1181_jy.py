import sys
input=sys.stdin.readline
n=int(input())
c=[]
e=[]
for i in range(n):
    d=input().strip()
    if d in e:
        continue
    else:    
        e.append(d)
        c.append([len(d),d])
for i in sorted(c):
    print(i[1])