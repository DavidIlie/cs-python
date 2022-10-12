# data = [1, 2, [3, 4], [5, 6], [5, [5, 12]]]
data = [1, 2, [3, 4], [5, 6]]


def getSum(piece):
    if len(piece) == 0:
        return 0
    elif type(piece[0]) is list:
        return getSum(piece[0]) + getSum(piece[1:])
    else:
        return piece[0] + getSum(piece[1:])


print(getSum(data))