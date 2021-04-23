import decrypt
from decrypt import decrpytText, encryptText

la = decrypt.iden("37","2")
la.identitas()

li = decrypt.nama("Abdullah Faqih Mubarak","Didi Suhardi","Felisiana Ardelia Azzahra","Zakia Marrit")
li.anggota()

basicAlphabet = "abcdefghijklmnopqrstuvwxyz" \
                "abcdefghijklmnopqrstuvwxyz" \
                "abcdefghijklmnopqrstuvwxyz"

newString = ""

originalText = input("\nOriginal Text: ")
print("Ori text: ", originalText)

choice = str(input("1. Encrypt \n2. Decrypt \nMasukan pilihan kamu:"))
if choice == "Encrypt" or choice == "1":
    sumChanged = 37
    encryptText(originalText, basicAlphabet, newString, sumChanged)
elif choice == "Decrypt" or choice == "2":
    sumChanged = -37
    decrpytText(originalText, basicAlphabet, newString, sumChanged)
else:
    print("Your choice sucks, restart the program")
