def makeForms(verb):
    x = slice(len(verb) - 1)
    if verb.endswith("y"):
        verb = verb[x] + "ies"
    elif verb.endswith("o") or verb.endswith("ch") or verb.endswith("s") or verb.endswith("sh") or verb.endswith("x") or verb.endswith("z"):
        verb = verb + "es"
    else:
        verb = verb + "s"
    print("Result: " + verb)
makeForms(input("Please input the word: "))