#input
l = [int(x) for x in input().split("+")]

# print(l)
# print(type(list))
l.sort()
for x in range(0,len(l)):
    if x == len(l)-1:
        print(l[x])
    else:
        print(l[x],end="+")
