def int_to_bin(n):
    n = int(n)
    
    b = ''

    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    print(b)

int_to_bin(30)
