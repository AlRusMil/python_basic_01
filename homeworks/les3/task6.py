def int_func(any_word: str) -> str:
    """
    The function takes a word and returns it with an uppercase first letter
    :param any_word: word to be changed
    :return: word with uppercase first letter
    """
    return any_word[0].upper() + any_word[1:]


def int_func_mas(words: str) -> str:
    """
    The function takes words and returns it with an uppercase first letter
    :param words: words to be changed
    :return: words with uppercase first letter
    """
    words_list = words.split(' ')
    result_words = ''
    for word in words_list:
        result_words += int_func(word) + ' '
    return result_words


while True:
    any_string = input("Введите строку либо -1, чтобы выйти из программы:\n")
    if any_string == '-1':
        print("Программа завершена!")
        break
    print(int_func_mas(any_string))
    print('-' * 30)
