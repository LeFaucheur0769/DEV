test = "Hello World"
key = "azertyuiopsdfghjklmwxcvbn"
alpha = "abcdefghijklmnopqrstuvwxyz"
testList = []
isnot = "a"


testList = list(test)

print(isnot not in alpha)

for i in range(len(testList)):
    if (isnot not in alpha) == True:
        print("not in")