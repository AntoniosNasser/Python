str = input("Enter one line of text to encrypt : ")
while True:
    try:
        num = int(input("Enter shift value between 1 and 25: "))
        if num < 1  or num > 25 :
            raise ValueError
        elif type(num) != int :
            raise  TypeError
        break
    except TypeError:
        print("plz Enter intger value")
    except ValueError:
        print("plz Enter a number between 1 and 25")


for i in str:
    if(i.isalpha == True):
        print(chr(ord(i)+num),end="")
    else:
        print(i,end="")