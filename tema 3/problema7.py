def set_operations(*sets):
    operations = {
        '|': 'union',
        '&': 'intersection',
        '-': 'difference',
    }

    result_dict = {}

    for i, set1 in enumerate(sets):
        for j, set2 in enumerate(sets):
            if i != j:  # Avoid comparing a set to itself
                for op, op_name in operations.items():
                    key = f"{set1} {op} {set2}"
                    if op == '|':
                        result = set1.union(set2)
                    elif op == '&':
                        result = set1.intersection(set2)
                    elif op == '-':
                        result = set1.difference(set2)
                    result_dict[key] = result

    return result_dict


set1 = {1, 2}
set2 = {2, 3}

result = set_operations(set1, set2)
for key, value in result.items():
    print(f"{key}: {value}")
