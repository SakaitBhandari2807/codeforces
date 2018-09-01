n = int(input())

co = n

count = 0 
while co>0:
    if co%10 == 4 or co%10 == 7:
        count += 1
    co //=10

if count == 4 or count == 7 or count == 47:
    print("YES")
else:
    print("NO")
