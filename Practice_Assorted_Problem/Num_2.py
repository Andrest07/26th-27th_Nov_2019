#def translate(text):
    #result = ""
    #for i in range(len(text)):
        #if not text[i] == "a" and not text[i] == "o" and not text[i] == "e" and not text[i] == "i" and not text[i] == "o" and not text[i] == "u" and not text[i] == " ":
            #result = result[0:i:1] + text[i] + "o" + text[i:len(text):1]
        #print(result)
    #return result
    #### A failure of an attempt to make the code shorter, wanted to see if there was a more efficient way (by avoiding the else part). On hindsight I'm not sure if my method would even work unless editted heavily....

def translate2(text):
    result = ""
    for i in range(len(text)):
        if not text[i] == "a" and not text[i] == "o" and not text[i] == "e" and not text[i] == "i" and not text[i] == "o" and not text[i] == "u" and not text[i] == " ":
            result = result + text[i] + "o" + text[i]
        else:
            result = result + text[i]
    return result
#print(translate(input("Please input the text: ")))
print(translate2(input("Please input the text: ")))