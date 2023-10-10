def list_operations(a: list, b: list) -> tuple[list, list, list, list]:
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return intersection, union, a_minus_b, b_minus_a

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection_result, union_result, a_minus_b_result, b_minus_a_result = list_operations(list_a, list_b)

print("Intersection:", intersection_result)
print("Union:", union_result)
print("Elements in A but not in B:", a_minus_b_result)
print("Elements in B but not in A:", b_minus_a_result)
