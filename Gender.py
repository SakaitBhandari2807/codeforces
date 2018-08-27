str = input()
list = list(str)

# print(list)

distinct = set(list)

# print(distinct)

if len(distinct)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")