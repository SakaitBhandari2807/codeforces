#input
groups = int(input())
peopleInEachGroup = [int(x) for x in input().split(" ")]

list =[0]*4
# print(list)

for x in peopleInEachGroup:
    # print(x)
    list[x-1]=list[x-1]+1

count=list[3]
count+=list[2]

if list[2]>list[0]:
    list[2]=0
    list[0]=0
elif list[2]<list[0]:
    list[0]-=list[2]
    list[2]=0
else:
    list[2]=0
    list[0]=0


count+=list[1]//2

if list[1]%2==0:
    list[1]=0
elif list[1]%2!=0:
    list[1]=1

if list[0]<=list[1]:
    count+=list[1]
    list[1]=0
elif list[0]>list[1]:
    sum=list[0]+list[1]
    count+=sum//4
    if sum%4<4 and sum%4!=0:
        count+=1

print(count)