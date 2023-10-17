global val
val = False
def passValid(inpPass):
    valid = True
    lenCheck = False
    alphanumCheck = False
    uppercaseCheck = False
    lowercaseCheck = False
    numberCheck = False
    specialCharacterCheck = False
    password = inpPass
    passSplit = ([*password])
    print(passSplit)

    len_pass = len(passSplit)

    if 8 < len_pass+1 < 20:
        lenCheck = True

    for i in range(len_pass):

        if ord(passSplit[i]) < 122:
            alphanumCheck = True
        if 65 <= ord(passSplit[i]) <= 90:
            uppercaseCheck = True
        if 97 <= ord(passSplit[i]) <= 122:
            lowercaseCheck = True
        if 48 <= ord(passSplit[i]) <= 57:
            numberCheck = True
        if ord(passSplit[i]) == 95 or ord(passSplit[i]) == 64 or ord(passSplit[i]) == 36:
            specialCharacterCheck = True

        if lenCheck == False or alphanumCheck == False or uppercaseCheck == False or lowercaseCheck == False or numberCheck == False or specialCharacterCheck == False:
            valid = False
        else:
            valid = True
            global val
            val = True

    if lenCheck == False:
        print("Only between 8 and 20 characters")
    if alphanumCheck == False:
        print("Only alphanumeric characters")
    if uppercaseCheck == False:
        print("Needs at least one uppercase letter")
    if lowercaseCheck == False:
        print("Needs at least one lowercase letter")
    if numberCheck == False:
        print("Needs at least one number")
    if specialCharacterCheck == False:
        print("Needs at least one special character _, @, $")
    if valid == False:
        print("\n" + '\033[4m' +"Invalid, Please change password" + '\033[4m' +'\033[0m' + '\033[0m')



# print(ord("a"))
while val == False:
    password = str(input("Enter password: "))
    passValid(password)

print('\033[1m' + "Password Success!" + '\033[1m')




#
# word = "string"
# wordSplit = ([*word])
# print(wordSplit)
