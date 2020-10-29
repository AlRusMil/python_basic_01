some_list = [1, 5, "ffffgede", 0, True, [1, "r3r3r3"], "fefe", (1, ), (1, 5), {1:"as", "eee":"4343"}]

for item_index in range(len(some_list)):
    print(f'{item_index}й элемент - {some_list[item_index]} является: {type(some_list[item_index])}')