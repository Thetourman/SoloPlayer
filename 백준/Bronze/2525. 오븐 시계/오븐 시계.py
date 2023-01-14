h,m = map(int, input().split())
n = int(input())
ht = n//60
mt = n%60

if n>59:
  h+=ht
  m+=mt
  if h >= 24:
    h = h%24
  if m >= 60:
    h += 1
    m -= 60
    if h >= 24:
      h = h%24
else:
  m += n
  if m>59:
    h += 1
    m -= 60
    if h>=24:
       h = h%24

print(h,m)