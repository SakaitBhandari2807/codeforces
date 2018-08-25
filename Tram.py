stops = int(input())

passenger=0
maxCapacity = 0 
for i in range(0,stops):
    a,b = [int(x) for x in input().split(' ')]
    #print(a,b)
    passenger = (passenger-a)+b
    if maxCapacity<passenger:
        maxCapacity=passenger
print(maxCapacity)
