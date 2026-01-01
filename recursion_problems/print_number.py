# Print N to 1 and 1 to N

def print_n_to_1(n):
    if n==1:
        print(n)
    else:
        print(n)
        print_n_to_1(n-1)


print_n_to_1(10)
