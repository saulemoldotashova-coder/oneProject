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
