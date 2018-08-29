n = int(input())

vectors = [0]*n
for i in range(0,n):
    vectors[i] = [int(x) for x in input().split(" ")]

x_cord_sum = 0
y_cord_sum = 0
#print(vectors)

for x in range(0,n):
    x_cord_sum += vectors[x][0]
    y_cord_sum += vectors[x][1]
    
if x_cord_sum == 0 and y_cord_sum==0:
    print("YES")
else:
    print("NO")
    



