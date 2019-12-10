def islower(c):
    '''
    Validate is c is uppercase or lowercase

    :param char c: Letter to validate
    :type c: character or None
    :return: True or false
    :rtype: bool
    '''
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
