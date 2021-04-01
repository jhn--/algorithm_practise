def sqrt(x):
    y = 0
    while x - y**2 > 0.01:
        y += 0.1
        print(y)
    return y
