def checkPalindrome(string):
    lst = []
    count = 0
    if string == "":
        return False
    else:
        string.lower()
    for i in string:
        if i == " ":
            continue
        else:
            lst.append(i)
            count +=1
    for j in range(len(lst)):
        if lst[j] != lst[count - (j+1)]:
            return False
    return True


str = input("Enter some text : ")
Cvalue = checkPalindrome(str)
if Cvalue == True:
    print("It's a palindrome")
elif Cvalue == False :
    print("It's not a palindrome")