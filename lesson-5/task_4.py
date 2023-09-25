# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы), и возвращает
# самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

import re


def get_longest_word(s: str):

    if not re.match(r'^[a-zA-z\s]+$', s):
        return 'Please, enter the valid string'
    words = s.split()
    return max(words, key=len)


result = get_longest_word('get the longest word')
assert result == 'longest'

# result = get_longest_word('getthelongestword')
# assert result == 'getthelongestword'

# result = get_longest_word('один два три четыре')
# assert result == 'Please, enter the valid string'

# result = get_longest_word('1234567890.^$*+?{}[]\|()')
# assert result == 'Please, enter the valid string'
