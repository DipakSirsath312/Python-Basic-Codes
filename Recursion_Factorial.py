def facto(n):
    if(n == 1 or n == 0):
        return 1
    return facto(n-1) * n

print(facto(5))