# 5 задание. Удалить повторяющиеся элементы из последовательности, сохраняя порядок.

def unique_in_order(sequence):
    result = []

    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)

    return result