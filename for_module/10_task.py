# 10 задание. Посчитать, сколько раз каждый символ встречается в строке.

def count(s):
    result = {}

    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result 