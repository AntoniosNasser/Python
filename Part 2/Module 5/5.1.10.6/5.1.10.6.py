def getDigitsInNumber(num):
    count = 0
    n = num
    lst = []
    while (n > 0):
        count = count + 1
        n = n // 10
    for i in range(count):
        lst.append(num // (10 ** (count - (i + 1))))
        num = num - lst[i] * 10 ** (count - (i + 1))
    return lst

def drawFirstRow(digit):
    if   digit == 0 or digit == 2 or digit == 3 or digit == 5 or digit == 6 or digit == 7 or digit == 8 or digit == 9:
        print("###",end=" ")
    elif digit == 1:
        print("  #",end=" ")
    else:
        print("# #",end=" ")

def drawSecondRow(digit):
    if digit == 1 or digit == 2 or digit == 3 or digit == 7 :
         print("  #",end=" ")
    elif digit == 4 or digit == 8 or digit == 9 or digit == 0:
         print("# #",end=" ")
    else:
        print("#  ",end=" ")

def drawThirdRow(digit):
     if digit == 2 or digit == 3 or digit == 4 or digit == 5 or digit == 6 or digit == 8 or digit == 9:
         print("###",end=" ")
     elif digit == 1 or digit == 7:
         print("  #",end=" ")
     else:
         print("# #",end=" ")

def drawFourthRow(digit):
    if digit == 1 or digit == 3 or digit == 4 or digit == 5 or digit == 7 or digit == 9 :
         print("  #",end=" ")
    elif digit == 6 or digit == 8 or digit == 0:
         print("# #",end=" ")
    else:
         print("#  ",end=" ")

def drawFifthRow(digit):
     if digit == 2 or digit == 3 or digit == 5 or digit == 6 or digit == 8 or digit == 9 or digit == 0:
         print("###",end=" ")
     else:
         print("  #",end=" ")


def ledDisplay(lstOfnum):
    for i in range(len(lstOfnum)):
        drawFirstRow(lstOfnum[i])
    print("\n")
    for i in range(len(lstOfnum)):
        drawSecondRow(lstOfnum[i])
    print("\n")
    for i in range(len(lstOfnum)):
        drawThirdRow(lstOfnum[i])
    print("\n")
    for i in range(len(lstOfnum)):
        drawFourthRow(lstOfnum[i])
    print("\n")
    for i in range(len(lstOfnum)):
        drawFifthRow(lstOfnum[i])
    print("\n")
num = int(input("Enter number to display : "))
ledDisplay(getDigitsInNumber(num))


