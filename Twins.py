n = int(input())
coins = [int(x) for x in input().split(" ")]

cl = [0]*(n-1)
coins.sort()

#print(coins)

cl.insert(0,coins[0])
for x in range(1,n):
    cl[x]=cl[x-1]+coins[x]
#print(cl)

clr = [0]*(n-1)
clr.insert(n-1,coins[n-1])
for x in range(n-2,-1,-1):
    clr[x] = clr[x+1]+coins[x]
#print(clr)

index = 0
for i in range(0,n-1):
    diff = 10000
    if cl[i]<clr[i+1]:
        if diff > abs(cl[i]-clr[i+1]):
            diff = abs(cl[i]-clr[i+1])
            #print(diff)
            index = n-(i+1)
if index == 0:
    print(n)
else:
    print(index)





