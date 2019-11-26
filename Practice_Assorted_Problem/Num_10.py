import string
def pangram(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in x.lower():
            p = False
        else:
            p = True
    if p == False:
        print("It is not a pangram.")
    else:
        print("It is a pangram.")
pangram(input("Please input a sentence: "))