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

def unique_in_order(sequence):
    result = []

    for item in sequence:
        if not result or item != result[-1]:
            result.append(item)

    return result

# 6 задание 

def friend(x):
    result = []

    for name in x:
        if len(name) == 4:
            result.append(name)

    return result 

# 7 задание 

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# 8 задание 

def bouncing_ball(h, bounce, window):
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1

    count = 0

    while h > window:
        count += 1
        h *= bounce

        if h > window:
            count += 1

    return count 

# 9 задание 

def delete_nth(order, max_e):
    counts = {}
    result = []

    for num in order:
        counts[num] = counts.get(num, 0)

        if counts[num] < max_e:
            result.append(num)
            counts[num] += 1

    return result


# 10 задание 

def count(s):
    result = {}

    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result 

# 11 задание 

def solution(s):
    if len(s) % 2 != 0:
        s += '_'

    result = []

    for i in range(0, len(s), 2):
        result.append(s[i:i+2])

    return result 

# 12 задание 

def solution(number):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    result = ""

    for i in range(len(values)):
        while number >= values[i]:
            result += symbols[i]
            number -= values[i]

    return result 

# 13 задание 

def ips_between(start, end):
    def ip_to_int(ip):
        parts = list(map(int, ip.split(".")))
        
        return (
            parts[0] * 256**3 +
            parts[1] * 256**2 +
            parts[2] * 256 +
            parts[3]
        )
    
    return ip_to_int(end) - ip_to_int(start)  

# 14 задание 

def first_non_repeating_letter(s):
    for char in s:
        if sum(c.casefold() == char.casefold() for c in s) == 1:
            return char
    return ''

# 15 задание 

def dir_reduc(arr):
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "WEST": "EAST",
        "EAST": "WEST"
    }

    result = []

    for direction in arr:
        if result and result[-1] == opposites[direction]:
            result.pop()
        else:
            result.append(direction)

    return result 