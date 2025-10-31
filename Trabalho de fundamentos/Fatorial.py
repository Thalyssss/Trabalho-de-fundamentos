def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(f"Fatorial de 4 é: {fatorial(4)}")