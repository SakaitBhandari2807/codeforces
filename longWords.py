t = int(input())
while t>0:
    s = input()
    l = len(s)
    out=""
    if l>10:
         out= s[0]+str(l-2)+s[l-1]
         print(out)
    else:
        print(s)
    t-=1