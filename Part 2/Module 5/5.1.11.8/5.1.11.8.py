def removeSpaces(str):
    strlst = []
    for i in str:
        if i == " ":
            continue
        else:
            strlst.append(i)
    return strlst

def checkAnagrams(string):
    strlst = string.split("    ")
    str1, str2 = strlst[0], strlst[1]
    strlst1, strlst2 = [],[]
    if str1 == "" or str2 =="":
        return False
    else:
        str1.lower()
        str2.lower()
        strlst1, strlst2 = removeSpaces(str1), removeSpaces(str2)
    #print(strlst1)
    #print(strlst2)
    if len(strlst1) == len(strlst2):
        #print("length equal")
        for i in strlst1:
            #print("i")
            if i not in strlst2:
                #print("Not found")
                return False
            else:
                #print("found")
                continue
        return True
    else:
        return False


str = input("Enter two texts seprated with tab : ")
if checkAnagrams(str):
    print("Anagrams")
else:
    print("Not anagrams")
