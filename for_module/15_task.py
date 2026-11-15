# 15 задание. Сократить массив направлений, удаляя противоположные направления, которые следуют друг за другом.

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
