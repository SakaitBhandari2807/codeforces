l,b,a = [int(x) for x in input().split(" ")]

# print(l,type(l))
# print(b,type(b))
# print(a,type(a))

rows=0
col=0

if l>a:
    rows=l//a
    if l%a!=0:
        rows+=1
elif l<=a:
    rows+=1

# print(rows)

if b>a:
    col=b//a
    if b%a!=0:
        col+=1
elif b<=a:
    col+=1

# print(col)

print(rows*col)



