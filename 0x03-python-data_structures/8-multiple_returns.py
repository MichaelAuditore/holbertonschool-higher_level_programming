#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is "":
        return (0, None)
    else:
        for i in sentence:
            return (len(sentence), i)
