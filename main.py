from decrypt import decrpytText, encryptText

basicAlphabet = "abcdefghijklmnopqrstuvwxyz" \
                "abcdefghijklmnopqrstuvwxyz" \
                "abcdefghijklmnopqrstuvwxyz"

newString = ""

originalText = input("Original Text: ")
print("Ori text: ", originalText)

choice = str(input("1. Encrypt or 2.Decrypt :"))
if choice == "Encrypt" or choice == "1":
    sumChanged = 37
    encryptText(originalText, basicAlphabet, newString, sumChanged)
elif choice == "Decrypt" or choice == "2":
    sumChanged = -37
    decrpytText(originalText, basicAlphabet, newString, sumChanged)
else:
    print("Your choice sucks, restart the program")
