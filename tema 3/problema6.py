def count_unique_and_duplicate_elements(input_list):
    unique_elements = set()
    duplicate_elements = set()

    for item in input_list:
        if item in unique_elements:
            duplicate_elements.add(item)
        else:
            unique_elements.add(item)

    return len(unique_elements), len(duplicate_elements)

my_list = [1, 2, 2, 3, 4, 4, 5, 5, 6]

unique_count, duplicate_count = count_unique_and_duplicate_elements(my_list)
result_tuple = (unique_count, duplicate_count)
print(result_tuple)
