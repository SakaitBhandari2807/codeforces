inpStr = input().lower()

vowels = ['a','e','i','o','u','y']

#printing the values
#print(inpStr)
#print(vowels)

opStr=""
for x in inpStr:
    if x not in vowels:
        opStr+="."+x


print(opStr)
