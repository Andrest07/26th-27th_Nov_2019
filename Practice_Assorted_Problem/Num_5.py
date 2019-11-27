def overlapping():
    f = False
    m1 = int(input("How many values for the first list? "))
    lst1 = [None] * m1
    m2 = int(input("How many values for the second list? :"))
    lst2 = [None] * m2
    for i in range(m1):
        lst1[i] = input("Input the first list's value(s): ")
    for i in range(m2):
        lst2[i] = input("Input the second list's value(s): ")
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            if lst1[i] == lst2[j]:
                f = True
    print("List 1: " + str(lst1))
    print("List 2: " + str(lst2))
    print(f)
overlapping()