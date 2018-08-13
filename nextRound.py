n,k = [int(x) for x in input().split(" ")]
scores = [int(x) for x in input().split(" ")]

#print commands
# print(n,k)
# print(scores)

c = 0
for score in scores:
    if score>=scores[k-1] and score>0:
        c+=1

# print(type(count))
print(c)

# print(output)
