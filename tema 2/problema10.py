def combine_lists(*lists: list) -> list[tuple]:
    max_length = max(len(lst) for lst in lists)
    result = []

    for i in range(max_length):
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result.append(combined_tuple)

    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

combined = combine_lists(list1, list2, list3)
print(combined)
