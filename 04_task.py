# 4 задание 

def narcissistic(value):
    digits = str(value)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    if total == value:
        return True
    else:
        return False 