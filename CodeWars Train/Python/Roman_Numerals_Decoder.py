num = "XXI"
end = 0


def solution(roman):

    end = 0
    for i in range(len(roman)):
        if(len(roman) == 1):
            end = end + 1
        else:
            if roman[i] == "X":
                if roman[i - 1] == "I":
                    end = end + 9
                else:
                    end = end + 10
            if roman[i] == "V":
                if roman[i - 1] == "I":
                    end = end + 4
                else:
                    end = end + 5
            if roman[i] == "I":
                if roman[i + 1] == "X" or roman[i + 1] == "V" or roman[i + 1] == "M":
                    None
                else:
                    end = end + 1
            if roman[i] == "M":
                if roman[i - 1] == "I":
                    end = end + 999
                else:
                    end = end + 1000
            if roman[i] == "D":
                if roman[i - 1] == "I":
                    end = end + 499
                else:
                    end = end + 500
            if roman[i] == "L":
                if roman[i - 1] == "I":
                    end = end + 49
                else:
                    end = end + 50
            if roman[i] == "C":
                if roman[i - 1] == "I":
                    end = end + 99
                else:
                    end = end + 100
    return end


solution(num)
