def sum_series(n):
    if n < 1:
        return 0
    else:
        return n + sum_series(n - 2)


print("sum of positive integer 6:", sum_series(6))
print("sum of positive integer 10:", sum_series(10))