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

def temp_name():
    ifTrue = True
    while ifTrue == False:
        howMany = input("How many name do you want : ")
        if howMany.isnumeric() == True:
            for i in howMany:
                name = names.get_full_name()
                save.write(name)
            ifTrue = True
        else:
            print("Please a numeric value !!")

print("\033[H\033[J")
while exitLoop == False:
    try:
        storeFile = input("\tWould you store your new name (y/n) : ").lower()
        if storeFile == "y" or storeFile == "n":
            if storeFile == "y":
                filePath = input("Where would you store your results : ")
                writeOrAppend = input(" a to append and w to wipe and write, by default it's a : ").lower()
                if writeOrAppend == "w":
                    save = open(filePath, writeOrAppend)
                    temp_name()
                else:
                    save = open(filePath, "a")
                    temp_name()
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
