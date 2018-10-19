#337/A
#Problem name: Puzzles
def findMin(a,b):
    if a>=b:
        return b
    else:
        return a

students,puzzles = [int(x) for x in input().split(" ")]
pieces = [int(x) for x in input().split(" ")]
pieces.sort()
min = 999999999
i = 0;
while i<=puzzles-students:
    if min > pieces[i+students-1] - pieces[i]:
        min = pieces[i+students-1] - pieces[i]
    i += 1
print(min)