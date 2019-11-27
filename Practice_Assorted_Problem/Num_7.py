def wordlength():
    m = int(input("How many words? "))
    words = [None] * m
    for i in range(m):
        words[i] = input("Input the words: ")
    for i in range(m):
        print(len(words[i]))
wordlength()