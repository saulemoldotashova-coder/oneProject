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