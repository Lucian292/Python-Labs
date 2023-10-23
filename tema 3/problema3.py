def compare_dicts(dict1, dict2):
    # Check if the types of the two objects are different
    if type(dict1) != type(dict2):
        return False

    # Check if both objects are dictionaries
    if isinstance(dict1, dict):
        # Check if the keys are the same
        if set(dict1.keys()) != set(dict2.keys()):
            return False

        # Recursively compare the values
        for key in dict1:
            if not compare_dicts(dict1[key], dict2[key]):
                return False

    # If the objects are not dictionaries, compare them using the equality operator
    else:
        if dict1 != dict2:
            return False

    return True

dict1 = {'a': 1, 'b': [1, 2, {'x': 3}], 'c': {'luci': 'lucian'}}
dict2 = {'a': 1, 'b': [1, 2, {'x': 3}], 'c': {'luci': 'lucian'}}
dict3 = {'a': 1, 'b': [1, 2, {'x': 4}], 'c': {'luci': 'loochee'}}

result1 = compare_dicts(dict1, dict2)
result2 = compare_dicts(dict1, dict3)

print(result1)  # True
print(result2)  # False
