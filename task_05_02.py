"""

"""


def get_quadrant_number(x,y):
    if x == 0 and y ==0:
        raise ValueError()
    if x > 0:
        if y > 0 :
            res = 1
        else:
            res = 4
    else:
        if y>0:
            res = 2
        else:
            res = 3

    return res
