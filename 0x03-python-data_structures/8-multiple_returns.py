#!/usr/bin/python3
def multiple_returns(sentence):
    tu = ()
    if len(sentence) == 0:
        tu = (0, None)
        return tu
    else:
        tu = (len(sentence), sentence[0])
        return tu
