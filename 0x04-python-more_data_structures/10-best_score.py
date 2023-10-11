#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or 0:
        return None
    first = 0
    for k, v in a_dictionary.items():
        if first < v:
            first = v
            key = k
    return key
