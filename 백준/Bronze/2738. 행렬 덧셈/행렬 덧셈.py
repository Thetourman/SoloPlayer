import sys

n,m = map(int,sys.stdin.readline().split())
b = []
c = []
for i in range(n):
    i = list(map(int,sys.stdin.readline().split()))
    b.append(i)
for i in range(n):
    i = list(map(int,sys.stdin.readline().split()))
    c.append(i)
for i in range(n):
    for s in range(m):
        print(b[i][s]+c[i][s],end=' ')
    print()