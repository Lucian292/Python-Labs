def generate_character_lists(x=1, string_list=None, flag=True) -> list[list[str]]:
    if string_list is None:
        string_list = []

    result_lists = []

    for string in string_list:
        char_list = []
        for char in string:
            ascii_code = ord(char)
            if (ascii_code % x == 0 and flag) or (ascii_code % x != 0 and not flag):
                char_list.append(char)
        result_lists.append(char_list)

    return result_lists

x = 2
string_list = ["test", "hello", "lab002"]
flag = False

result = generate_character_lists(x, string_list, flag)
print(result)
