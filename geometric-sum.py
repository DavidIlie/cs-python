def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2, n)) + geometric_sum(n - 1)


print("the geometric sum of 7:", geometric_sum(7))
print("the geometric sum of 4:", geometric_sum(4))