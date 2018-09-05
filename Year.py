Copy
year = int(input())

y = year+1
count = dict()
yr = y

while yr>year:
    #print("year:",yr,"y:",y)
    while y > 0:
        r = y%10
        y //= 10
        if r not in count.keys():
            count[r] = 1
        else:
            count[r] += 1
    y = yr+1
    if len(count.keys()) == 4:
        break;
    yr += 1
    count.clear()
print(yr)


