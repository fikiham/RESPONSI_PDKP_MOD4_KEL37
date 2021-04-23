basicAlphabet = "abcdefghijklmnopqrstuvwxyz" \
                "abcdefghijklmnopqrstuvwxyz"
newString = ""
sumChanged = 37
oriText = input("Original Text: ")
print("Ori text: ", oriText)
for i in range(len(oriText)):
    if not oriText[i].isalpha():
        newString += oriText[i]
    else:
        newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
print("newstring :", newString)
