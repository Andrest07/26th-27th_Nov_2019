#def char_freq(string):
    #lst = [[None] for i in range(len(string))]
    #f1 = 0
    #for i in range(len(string)):
        #f = False
        #for j in range(len(lst)):
            #print(i)
            #if not string[i][0] == lst[j][0]:
                #f = False
            #else:
                #v = j
                #f = True
        #if f == False:
            #lst.append(string[i])
            #lst[f1].append(1)
            #f1 += 1
        #else:
            #lst[v].append(lst[v][0] + 1)
    #for i in range(len(lst)):
        #print(str(lst[i]) + ": " + str(lst[i][0]))
    #### Doesn't work for some reason... Was trying to do a list inside a list like lst = [a[1], b[3], c[2]]. Visual Basic's multidimensional arrays are so much easier to play with....

def char_freq2(string): #boring simpler way, treats upper and lowercase letters as equal.
    lst = [] * len(string)
    lst2 = [] * len(string)
    f1 = 0
    for i in range(len(string)):
        f = False
        for j in range(len(lst)):
            if not string[i].upper() == lst[j].upper():
                f = False
            else:
                v = j
                f = True
        if f == False:
            lst.append(string[i].upper())
            lst2.append(1)
            f1 += 1
        else:
            lst2[v] = lst2[v] + 1
    for i in range(len(lst)):
        print(str(lst[i].upper()) + ": " + str(lst2[i]))
#char_freq(input("Input string: "))
char_freq2(input("Input string: "))