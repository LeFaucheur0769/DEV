import random

passwd = ""
listLower = "abcdefghojklmnopqrstuvwxyz"
listUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
listNum = "1234567890"
listSp = "&é'()-è_çà=$ù^*!:;,?./§%µ"
iteration = 25
entropie = 10
try:
    entropie = int(input("The entropie (max 100) : "))
    if entropie >= 100:
        print("Number to high")
        exit()
    iteration = int(input("The iteration : "))
except ValueError:
    print("Error")
    exit()

for i in range(iteration):
    LUNS = random.randint(1, 4)
    if LUNS == 1:
        r = random.randint(1, len(listLower))
        passwd += listLower[r - 1 : r]
    elif LUNS == 2:
        r = random.randint(1, len(listNum))
        passwd += listNum[r - 1 : r]
    elif LUNS == 3:
        r = random.randint(1, len(listSp))
        passwd += listSp[r - 1 : r]
    elif LUNS == 4:
        r = random.randint(1, len(listUpper))
        passwd += listUpper[r - 1 : r]
    else:
        exit()
print(passwd)
