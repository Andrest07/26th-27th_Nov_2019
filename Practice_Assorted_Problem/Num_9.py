def filter_long_words():
    try:
        m = int(input("How many words would you like to input? "))
        n = int(input("Please input the amount of letters: "))
        x = [None] * m
    except:
        TypeError("Only integers are allowed.")
    for i in range(m):
        x[i] = input("Please input a word: ")
    for i in range(m):
        if len(x[i]) == n:
            print(x[i], end=", ")
filter_long_words()