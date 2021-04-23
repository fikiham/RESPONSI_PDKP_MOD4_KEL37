class iden:
    def __init__(iden, kelompok, shift):
        iden.kelompok = kelompok
        iden.shift = shift
    def identitas(iden):
        print(f"Kelompok = {iden.kelompok}\nShift = {iden.shift}")

class nama:
    def __init__(nama, nama1,nama2,nama3,nama4):
        nama.nama1 = nama1
        nama.nama2 = nama2
        nama.nama3 = nama3
        nama.nama4 = nama4
    def anggota(nama):
        print(f"Anggota 1 = {nama.nama1}\nAnggota 2 = {nama.nama2}\nAnggota 3 = {nama.nama3}\nAnggota 4 = {nama.nama4}")
        print("\n————————————Responsi Modul 4————————————")

def decrpytText(oriText,basicAlphabet,newString, sumChanged):
    for i in range(len(oriText)):
        if not oriText[i].isalpha():
            newString += oriText[i]
        elif oriText[i].isupper():
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i].lower()) + sumChanged].upper()
        else:
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
    print("\nKalimat kamu berhasil di dekripsikan menjadi:", newString)

def encryptText (oriText,basicAlphabet,newString, sumChanged):
    for i in range(len(oriText)):
        if not oriText[i].isalpha():
            newString += oriText[i]
        elif oriText[i].isupper():
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i].lower()) + sumChanged].upper()
        else:
            newString = newString + basicAlphabet[basicAlphabet.index(oriText[i]) + sumChanged]
    print("\nKalimat kamu berhasil di enkripsikan menjadi:", newString)
