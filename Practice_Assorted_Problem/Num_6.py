#Don't judge me, I got hungry at this point.

def histogram():
    m = int(input("How many integers would you like? "))
    lst = [None] * m
    for i in range(m):
        lst[i] = int(input("Please input the integer: "))
    for i in range(m):
        for j in range(lst[i]):
            print("*", end="")
        print("")
histogram()