def validate_dict(rules, dictionary):
    # Create a set to store the keys that appear in the rules
    keys_in_rules = set(key for key, _, _, _ in rules)

    for key, value in dictionary.items():
        # Check if the key is not in the set of keys from the rules
        if key not in keys_in_rules:
            return False

        for rule in rules:
            rule_key, prefix, middle, suffix = rule
            if rule_key == key:
                if not value.startswith(prefix) or not value.endswith(suffix):
                    return False
                if middle not in value[1:-1]:  # Check middle inside the value (not at the beginning or end)
                    return False

    return True

# Example usage:
rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid",
    "key2": "start of winter is here"
}

result = validate_dict(rules, dictionary)
print(result)
