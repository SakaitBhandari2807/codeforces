str = input()


l = len(str)

#print(l)

flag = True

for i in range(0,l):
    if str[i] =='0':
        j = i+1
        count = 1
        while j<len(str)and str[j]!='1':
            j+=1
            count+=1
            if count == 7:
                flag = False
                break
    if not flag:
        break
    else:
        if str[i] == '1':
            j = i+1
            count = 1
            while j<len(str) and str[j]!='0':
                j+=1
                count+=1
                if count ==7:
                    flag = False
                    break
    if not flag:
        break
    
if flag:
    print("NO")
else:
    print("YES")



#def zero(str):
    
