# Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке

import hashlib


def count_diff_substring(string):
    len_substring = 1
    len_string = len(string)
    hash_substrings = set()
    while len_substring < len_string:
        for idx in range(len_string-len_substring+1):
            substring = string[idx:len_substring+idx]
            hash_substring = hashlib.sha1(substring.encode('utf-8')).hexdigest()
            hash_substrings.add(hash_substring)
        len_substring += 1

    return len(hash_substrings)


if __name__ == '__main__':
    user_str = input('Enter string: ')
    print(f'Count different substrings: {count_diff_substring(user_str)}')
