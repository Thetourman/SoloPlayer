h,m = map(int,input().split())
n = int(input())

h = h+n//60
m = m+n%60

if h>23:
  h-=24
if m>59:
  h+=1
  m-=60
  if h>23:
    h-=24

print(h,m)