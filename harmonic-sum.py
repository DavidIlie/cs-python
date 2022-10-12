def harmonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_sum(n - 1))


print("the harmonic sum of 7:", harmonic_sum(7))
print("the harmonic sum of 4:", harmonic_sum(4))