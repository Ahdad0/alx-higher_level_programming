#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = ()
    new_tuple_b = ()
    first = ()
    seconde = ()

    if len(tuple_a) < 2:
        if len(tuple_a) > 0:
            new_tuple_a = (tuple_a[0], 0)
        else:
            new_tuple_a = (0, 0)
    else:
        new_tuple_a = (tuple_a[0], tuple_a[1])

    if len(tuple_b) < 2:
        if len(tuple_b) > 0:
            new_tuple_b = (tuple_b[0], 0)
        else:
            new_tuple_b = (0, 0)
    else:
        new_tuple_b = (tuple_b[0], tuple_b[1])

    first = (new_tuple_a[0] + new_tuple_b[0])
    seconde = (new_tuple_a[1] + new_tuple_b[1])
    add_tuple = (first, seconde)
    return add_tuple
