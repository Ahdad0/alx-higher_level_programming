#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    first = 0
    for k, v in a_dictionary.items():
        if first < v:
            first = v
            key = k
    return key
