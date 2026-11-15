# 14 задание. Найти первый неповторяющийся символ в строке.

def first_non_repeating_letter(s):
    for char in s:
        if sum(c.casefold() == char.casefold() for c in s) == 1:
            return char
    return ''
