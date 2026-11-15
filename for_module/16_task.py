# 16 задание 

def arithmetic_sequence_elements(a, d, n):
    numbers = []
    
    for i in range(n):
        numbers.append(a + i * d)
        
    return ", ".join(map(str, numbers))  
