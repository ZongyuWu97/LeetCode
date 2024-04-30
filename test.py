def max_possible_value(arr):
    max_num = max(arr)  # Find the maximum element in the array
    max_bit = (
        len(bin(max_num)) - 2
    )  # Find the position of the most significant bit in the maximum element

    xor_value = (
        1 << max_bit
    ) - 1  # Create a number with all bits set up to the highest set bit
    while xor_value > max_num:
        max_bit -= 1
        xor_value = (1 << max_bit) - 1

    return xor_value


# Example usage:
arr = [8, 2, 4, 12, 1]
print(max_possible_value(arr))  # Output will be 14
