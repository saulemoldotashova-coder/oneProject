# 6 задание. Оставьте только имена друзей, у которых ровно 4 буквы в списке.

def friend(x):
    result = []

    for name in x:
        if len(name) == 4:
            result.append(name)

    return result 