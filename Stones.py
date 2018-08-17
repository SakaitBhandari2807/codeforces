n = int(input())

str = input()

count=0
i=1
while i<n:
    j=i+1
    if str[i-1]==str[i]:
        count+=1
        while(j<n and str[j]==str[j-1]):
            count+=1
            j+=1
    i = j
print(count)
