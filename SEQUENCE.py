#580/A
#problem name : Kefa and First Steps
n = int(input())
money = [int(x) for x in input().split(" ")]

#print(money)
i = 0
j =0
longestSequence = 1
currentLength = 1
while i < n-1:
    j = i+1
    currentLength = 1
    while j < n and money[j] >= money[j-1]:
        currentLength += 1
        j += 1
    #print(currentLength)
    if longestSequence < currentLength:
        longestSequence = currentLength
    i = j
print(longestSequence)
