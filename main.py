basicAlphabet = "abcdefghijklmnopqrstuvwxyz"
newString = ""
i=0
sumChanged =12
oriText = input("Original Text: ")
print ("Ori text: ",oriText)
while i <= len(oriText)-1:
  if not oriText[i].isalpha() and not oriText[i].isdigit():
    newString += oriText[i]
  else:
    newString += basicAlphabet[basicAlphabet.index(oriText[i]+sumChanged]
  i+=1
print ("newstring :",newString)
