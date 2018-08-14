n = int(input())

x = 0

while n>0:
    str = input()
    if '+' in str:
        x+=1
    elif '-' in str:
        x-=1
    n-=1

print(x)
        
