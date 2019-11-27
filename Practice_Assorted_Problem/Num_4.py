def is_member(val, m):
    v = [None] * m
    f = False
    for i in range(m):
        v[i] = input("Input list value(s): ")
    for i in range(m):
        if v[i] == val:
            f = True
    print(f)
is_member(input("Input value: "), int(input("How many values do you want? ")))
