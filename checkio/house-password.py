def checkio(data):
    digit = 0
    lower = 0
    upper = 0
    if len(data) > 0:
        for letter in data:
            if letter.isdigit():
                digit = 1
            elif letter.islower():
                lower = 1
            elif letter.isupper():
                upper = 1
        if digit == 1 and lower == 1 and upper == 1 and len(data) >= 10:
            return True
        else:
            return False
