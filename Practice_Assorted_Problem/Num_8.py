def find_longest_word():
    m = int(input("How many words do you want? "))
    lwords = [None] * m
    largest = ""
    f = False
    x = 0
    for i in range(m):
        lwords[i] = input("Please input the word:")
    while f == False:
        x = x + 1
        if x > m:
            f = True
        elif len(lwords[x - 1]) > len(largest):
            largest = lwords[x-1]
    print(largest + " is the longest word.")
find_longest_word()