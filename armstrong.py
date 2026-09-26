def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    n = len(digits)
    return sum(d**n for d in digits) == num