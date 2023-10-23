def find_mapping_loop(mapping):
    visited = set()
    result = []
    current_key = 'start'

    while current_key not in visited and current_key in mapping:
        visited.add(current_key)
        result.append(mapping[current_key])
        current_key = mapping[current_key]

    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = find_mapping_loop(mapping)
print(result)
