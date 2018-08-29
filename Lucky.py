number = int(input())

flag = True

if number%47==0 or number%4==0 or number%7==0:
   flag = True
else:
    n = number
    while n>0:
        if n%10==4 or n%10==7:
            n = n//10
        else:
            flag = False
            break
if flag:
    print("YES")
else:
    print("NO")


