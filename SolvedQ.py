p = int(input())

c = 0
while p>0:
    list = [int(x) for x in input().split(" ")]
    if list.count(1)>=2:
        c+=1
    p-=1

print(c)
        
