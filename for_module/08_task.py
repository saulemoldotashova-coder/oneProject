# 8 задание. Посчитать количество раз, которое мяч пройдет мимо окна при падении и отскоке.

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
