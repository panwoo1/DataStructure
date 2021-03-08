def gcd(a, b):
    while a*b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a+b


print(gcd(2, 4))