str = input()
#str = str.lower()


if str.isupper():
    print(str[0:].lower())
elif str[0].islower() and str[1:].isupper():
    print(str[0].upper(),end='')
    print(str[1:].lower())
elif len(str)==1 and str[0].islower():
    print(str[0].upper())
else:
    print(str)

