# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы), и возвращает
# самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

import re


def get_longest_word(s: str):

    if not re.match(r'^[a-zA-z\s]+$', s):
        return 'Please, enter the valid string'
    words = s.split()
    return max(words, key=len)


assert get_longest_word('get the longest word') == 'longest'
assert get_longest_word('getthelongestword') == 'getthelongestword'
assert get_longest_word('один два три четыре') == 'Please, enter the valid string'
assert get_longest_word('1234567890.^$*+?{}[]\|()') == 'Please, enter the valid string'