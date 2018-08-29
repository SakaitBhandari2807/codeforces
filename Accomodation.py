n = int(input())

rd = [0]*n

for x in range(0,n):
    rd[x] = [int(x) for x in input().split(" ")]

count = 0
for x in range(0,n):
    if rd[x][1] >= (rd[x][0]+2):
        count += 1
print(count)


