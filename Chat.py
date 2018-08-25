str = input()
l = len(str)
flag = True

if str.find('h') == -1:
    flag = False
else:
    for i in range(0,l):
        if str[i] == 'h':
            j = i+1
            while j<l and str[j]!= 'e':
                j+=1
            i = j
            if i<l and str[i] == 'e':
                j = i+1
                while j<l and str[j]!= 'l':
                    j+=1
                i = j
                if i<l and str[i] == 'l':
                    j = i+1
                    while j<l and str[j] != 'l':
                        j+=1
                    i = j
                    if i<l and str[i] == 'l':
                        j = i+1
                        while j < l and str[j] !='o':
                            j += 1
                        i = j
                        if i < l and str[i] == 'o':
                            break
                        else:
                            flag = False
                            break
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            else:
                flag = False
                break
        
if flag:
    print("YES")
else:
    print("NO")
