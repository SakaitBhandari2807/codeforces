#input
groups = int(input())
peopleInEachGroup = [int(x) for x in input().split(" ")]

list =[0]*4
# print(list)

count=0
for x in peopleInEachGroup:
    # print(x)
    list[x-1]=list[x-1]+1

count+=list[3]

if list[0]<list[2]:
    count+=lis[2]
elif list[0]>list[2]:
    count+=list[]
print(list)
