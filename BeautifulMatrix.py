matrix = [0]*5

ans = 0
for i in range(0,5):
    matrix[i] = [int(x) for x in input().split(' ')]
    for j in range(0,5):
        if matrix[i][j]==1:
            ans = abs(2-i)+abs(2-j)

print(ans)
