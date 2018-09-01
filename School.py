n,k = [int(x) for x in input().split(" ")]

str = list(input())


while k >0:
    i = 0
    while i < n-1:
        if str[i] == 'B' and str[i+1] == 'G':
            str[i] = 'G'
            str[i+1]='B'
            #print(str)
            i += 2
        else:
            i += 1
    k -= 1
print(''.join(str))
