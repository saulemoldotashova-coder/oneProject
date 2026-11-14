# 6 задание 

def friend(x):
    result = []

    for name in x:
        if len(name) == 4:
            result.append(name)

    return result 