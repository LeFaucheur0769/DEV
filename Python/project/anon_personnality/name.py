# documentation https://pypi.org/project/names/

### imports

import names
import time

###

### variables

gender = ""
storeFile = "n"
exitLoop = False

###
print("\033[H\033[J")
while exitLoop == False:
    try:
        storeFile = input("\tWould you store your new name (y/n) : ").lower()
        if storeFile == "y" or storeFile == "n":
            print(names.get_full_name(gender=gender))
            print(storeFile)
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
