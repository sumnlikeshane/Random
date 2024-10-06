def email_checker(check):
    if '@' in check and '.' in check:
        return ("Valid Email")
    else:
        return("Invalid Email")

print(email_checker(input()))