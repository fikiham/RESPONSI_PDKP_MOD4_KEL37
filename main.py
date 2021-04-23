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

originalText = input("\nMasukkan kalimat yang ingin anda ubah : ")
print("Kalimat asli: ", originalText)

#function enkripsi
def encryptText (oriText,basicAlphabet,newString, sumChanged):
    for i in range(len(oriText)):
        if not oriText[i].isalpha():
            newString += oriText[i]
        elif oriText[i].isupper():
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i].lower()) + sumChanged].upper()
        else:
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
    print("\nKalimat kamu berhasil di enkripsikan menjadi:", newString)


choice = str(input("1. Enkripsi \n2. Dekripsi \nMasukan pilihan kamu : "))
if choice == "Enkripsi" or choice == "1":
    sumChanged = 37
    encryptText(originalText, basicAlphabet, newString, sumChanged)
elif choice == "Dekripsi" or choice == "2":
    sumChanged = -37
    decrpytText(originalText, basicAlphabet, newString, sumChanged)
else:
    print("Pilihan yang anda masukkan tidak tersedia. Mohon ulang program.")
