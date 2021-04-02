def bisection(guess):
    """
    https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/lecture-videos/lecture-3-string-manipulation-guess-and-check-approximations-bisection/
    """
    ray = range(100)
    
    low = 0
    mid = len(ray)//2
    hih = len(ray)
    tries = 0
    if guess in ray and isinstance(guess,int):
        while mid != guess:
            tries += 1
            if guess > mid:
                print("guess too high")
                low = mid
                print(f'low: {low}')
            elif guess < mid:
                print("guess too low")
                hih = mid
                print(f'hih: {hih}')
            mid = (hih + low)//2 #key
            print(f'mid: {mid}')
        print(f"got it in {tries} tries.\n")
    else:
        print("number needs to be and integer from 0 to 99.")
