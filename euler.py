def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False 
    for p in range(3, n):
        if n % p == 0:
            return False
        p += 2
    return True