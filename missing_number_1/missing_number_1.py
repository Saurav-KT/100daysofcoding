def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * n + 1 // 2
    print(expected_sum)
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def find_missing_number_xor(arr):
    n = len(arr) + 1
    xor_result = 0
    for i in range(1, n + 1):
        xor_result ^= i
        # print(xor_result)

    for num in arr:
        xor_result ^= num

    return xor_result








find_missing_number_xor([1])

print(1^2)