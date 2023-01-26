n = int(input())
a = n//10
b = n%10
count = 0
while True:
    c = a+b
    n2 = (b*10)+c%10
    count += 1
    if n2 == n:
        break
    a = n2//10
    b = n2%10
        
print(count)