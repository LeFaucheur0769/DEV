import time
##

alpha = "abcdefghijklmnopqrstuvwxyz 0123456789&é'(-è_çà)=^$ù*,;:!¨£%µ?./§" ##the aplha
key = "qeyfmchoganlujxwbtkrzbvips 0123456789&é'(-è_çà)=^$ù*,;:!¨£%µ?./§"   ##the alpha key
keyList = [""]
alphaList = [""]

##

##

textC = "Hello World"   ##the text to encrypt
encrypted = ""  ##the text encrypted
decrypted = ""
textCList = []          ##the text to encrypt in list format
cryptOrDecrypt = "c"

##


##


alphaList = alpha.split()


keyList = key.split()

def crypt(lettre,keyVar):
    global encrypted
    for i in range(len(alpha)):
        if lettre == alpha[i]:
            encrypted = encrypted + keyVar[i]
        elif lettre == alpha[i].upper():
            encrypted = encrypted + keyVar[i].upper()
        elif (lettre not in alpha) == True and (lettre not in alpha.upper()) == True :
            if i == 1:
                encrypted = encrypted + lettre

def decrypt(lettre,keyVar):
    global decrypted
    if (lettre not in keyVar) == True and (lettre not in keyVar.upper()) == True :
        decrypted = decrypted + lettre
    else:
        for i in range(len(keyVar)):
            if lettre == keyVar[i]:
                decrypted = decrypted + alpha[i]
            elif lettre == keyVar[i].upper():
                decrypted = decrypted + alpha[i].upper()





print("\n\n\n\n\t\t\tVoici le traducteur raskayen 1.0\t\t\t\n\n\n")#intro 
while cryptOrDecrypt != "q":

    cryptOrDecrypt = input("\tVoulez vous crypter (c) ou décrypter (d) ou quitter (q) : ")
    if cryptOrDecrypt == "c":
        textC = input("\n\tVeuillez écrire votre message a crypter ici : ")
        print("\n\tEncryption en cours ", ".", ".",".",".")
        for i in range(len(textC)):
            crypt(textC[i], key)
        time.sleep(0.5)
        print("\n\n")
        print("Message crypté : ", encrypted, "\n\n\n\n")
        time.sleep(2.5)
    elif cryptOrDecrypt == "d" :
        textD = input("\n\tVeuillez écrire votre message a décrypter ici : ")
        print("\n\tDécryption en cours ", ".", ".",".",".")
        for i in range(len(textD)):
            decrypt(textD[i], key)
        time.sleep(0.5)
        print("\n\n")
        print("Message décrypté : ", decrypted, "\n\n\n\n")
        time.sleep(2.5)

print("\n\n\t\t\tAu revoir\n\n\n")
