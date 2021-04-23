def decrpytText(oriText,basicAlphabet,newString, sumChanged):
    for i in range(len(oriText)):
        if not oriText[i].isalpha():
            newString += oriText[i]
        else:
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
    print("newstring :", newString)

def encryptText (oriText,basicAlphabet,newString, sumChanged):
    for i in range(len(oriText)):
        if not oriText[i].isalpha():
            newString += oriText[i]
        else:
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
    print("newstring :", newString)

