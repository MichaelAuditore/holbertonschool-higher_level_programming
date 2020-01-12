#!/usr/bin/python3


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
            Text (String): a Text to print in a specific format

    TypeError:
            text must be a string

    Returns:
            not returns only print the text in specific format
    """
    idx = 0
    newstr = ""
    if text is None or type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        if i == " " and idx == 0:
            continue
        else:
            if i in ".?:":
                newstr += i + "\n\n"
                idx = 0
            else:
                newstr += i
                idx += 1
    revstr = ''.join(reversed(newstr))
    newstr = ""
    idx = 0
    for i in revstr:
        if i == " " and idx == 0:
            continue
        else:
            newstr += i
            idx += 1
    newstr = ''.join(reversed(newstr))
    print(newstr, end="")
