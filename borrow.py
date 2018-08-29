k,n,w = [int(x) for x in input().split(" ")]

borrow = 0
for x in range(0,w):
    borrow = borrow+k*(x+1)
if borrow>n:
    print(borrow-n)
else:
    print(0)
    