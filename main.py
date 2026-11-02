# 1 задание

def filter_list(l):
    num = len(l)
    list_new = []
    for i in range(num):
        if type(l[i]) == int:
            list_new.append(l[i])
    return list_new


print(filter_list([1,2,'a','b']))

# 2 задание 

def spin_words(text):
    words = text.split()
    result = []

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(result)


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))

# 3 задание 

def solution(str, ending):
    return str.endswith(ending) 

# 4 задание 

def narcissistic(value):
    digits = str(value)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)

    if total == value:
        return True
    else:
        return False

# 5 задание 
