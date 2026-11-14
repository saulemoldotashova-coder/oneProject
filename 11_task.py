# 11 задание 

def solution(s):
    if len(s) % 2 != 0:
        s += '_'

    result = []

    for i in range(0, len(s), 2):
        result.append(s[i:i+2])

    return result