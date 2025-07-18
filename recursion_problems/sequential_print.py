# print in ascending
def sequential_asc_order(i,n):
    if i>n:
        return
    print(i)
    sequential_asc_order(i+1,n)


# print in descending
def sequential_desc_order(i,n):
    if i<n:
        return
    print(i)
    sequential_desc_order(i-1,n)

# sequential_desc_order(10,1)

# print in increasing order
def sequential_asc_order_backtrack(i,n):
    if i<n:
        return
    sequential_asc_order_backtrack(i-1,n)
    print(i)

# sequential_asc_order_backtrack(10,1)

#print in decreasing order
def sequential_desc_order_backtrack(i,n):
    if i>n:
        return
    sequential_desc_order_backtrack(i+1,n)
    print(i)

sequential_desc_order_backtrack(1,10)