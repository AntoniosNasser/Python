def Isonedigit(num):
    if num < 10 and num > 0 and type(num) == int:
        return True
    else:
        return False

def calDigitOfLife(string):
    while True:
        digitNum = 0
        for i in string:
            digitNum += int(i)
        if Isonedigit(digitNum) == True:
            return digitNum
        else:
            string = str(digitNum)


digitStr = input("Enter your Birthdat at form YYYYMMDD : ")
print(calDigitOfLife(digitStr))