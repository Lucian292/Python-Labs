def count_matching_args(*args, **kwargs):
    matching_count = 0
    arg_values = set(args)
    kwarg_values = set(kwargs.values())

    for arg_value in arg_values:
        if arg_value in kwarg_values:
            matching_count += 1

    return matching_count

result = count_matching_args(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)
