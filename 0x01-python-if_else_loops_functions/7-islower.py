def islower(c):
    # Validate if a letter is upper or lower
    #
    # Return True is lowercase or False is upper
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
