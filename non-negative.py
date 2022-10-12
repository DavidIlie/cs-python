def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n / 10))


print("non-negative integer 345 is:", sumDigits(345))
print("non-negative integer 45 is:", sumDigits(45))