def list_set_operations(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a & set_b  # a intersected with b
    union = set_a | set_b  # a united with b
    a_minus_b = set_a - set_b  # a - b
    b_minus_a = set_b - set_a  # b - a

    result = [intersection, union, a_minus_b, b_minus_a]
    return result

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

result = list_set_operations(a, b)
print(result)
