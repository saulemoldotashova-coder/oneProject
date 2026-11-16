# 16 задание. Сформировать арифметическую последовательность из n элементов, начиная с числа a и с разностью d.

def arithmetic_sequence_elements(a, d, n):
    numbers = []
    
    for i in range(n):
        numbers.append(a + i * d)
        
    return ", ".join(map(str, numbers))  
