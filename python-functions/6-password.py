#!/usr/bin/python3
def validate_password(password):
    if len(password) < 8:
        return False
    check_upper = 0
    check_lower = 0
    check =  0
    while check < len(password):
        if(password[check].isupper()):
            check_upper += 1
        if (password[check].islower()):
            check_lower += 1
        if(password[check] == " "):
            return False
        check += 1
    if not (any(map(str.isdigit, password))):
        return False
    if check_upper < 1:
        return False
    if check_lower < 1:
        return False
print (validate_password("abcdE2uz"))