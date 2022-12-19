# documentation https://pypi.org/project/names/

### imports

import names
import time

###

### variables

gender = ""
storeFile = "n"
exitLoop = False
filePath = ""
writeOrAppend = ""

###
print("\033[H\033[J")
while exitLoop == False:
    try:
        storeFile = input("\tWould you store your new name (y/n) : ").lower()
        if storeFile == "y" or storeFile == "n":
            if storeFile == "y":
                filePath = input("Where would you store your results : ")
                writeOrAppend = input("By default, it will ")
                save = open(filePath, "a")
        elif storeFile == "exit":
            exitLoop = True
            print("\n\n\t\t Good bye\n\n")
            time.sleep(1.5)
        else:
            print("\tYou write something wrong")
    except KeyboardInterrupt:
        print("\033[H\033[J")
        print("Use exit to exit")
        time.sleep(1.5)
        print("\033[H\033[J")
