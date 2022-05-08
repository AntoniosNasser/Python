def readint(prompt, min, max):
    while True:
        try:
            num = int(input(prompt))
        except ValueError:
            print('Error: wrong input')
        if num > min and num < max:
            return num
        else:
            print('Error: the value is not within permitted range (', min, '..', max, ')')


v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)