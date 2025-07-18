def sum_n_number(n):
    if n == 0:
        return n
    else:
        return n + sum_n_number(n - 1)


# print(sum_n_number(3))
