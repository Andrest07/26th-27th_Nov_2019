def makeForming(verb):
    if verb.endswith("ie"):
        verb = verb[0:len(verb)-2] + "ying"
    elif verb.endswith("e") and not verb == "be" and not verb == "see" and not verb == "flee" and not verb == "knee":
        verb = verb[0:len(verb)-1] + "ing"
    elif (verb.endswith("a") or verb.endswith("o") or verb.endswith("e") or verb.endswith("i") or verb.endswith("u"))\
        and (not verb[len(verb)-2: len(verb)-1] == "a" or not verb[len(verb)-2: len(verb)-1] == "o"
        or not verb[len(verb)-2: len(verb)-1] == "e" or not verb[len(verb)-2: len(verb)-1] == "i"
        or not verb[len(verb)-2: len(verb)-1] == "u") and (verb[len(verb)-3: len(verb)-2] == "a" or
        verb[len(verb)-3: len(verb)-2] == "o" or verb[len(verb)-3: len(verb)-2] == "e" or
        verb[len(verb)-3: len(verb)-2]== "i" or verb[len(verb)-3: len(verb)-2] == "u"):
        verb = verb + verb[len(verb)-1] + "ing"
    else:
        verb = verb + "ing"
    print("Result: " + verb)
makeForming(input("Please input the word: "))