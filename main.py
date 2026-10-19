# 1 задание

def filter_list(l):
    num = len(l)
    list_new = []
    for i in range(num):
        if type(l[i]) == int:
            list_new.append(l[i])
    return list_new


print(filter_list([1,2,'a','b']))