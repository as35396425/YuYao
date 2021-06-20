def f(n):
    if n>1:
        return f(n-1)+f(n//2)
    elif n==1:
        return n+1

print(f(int(input())))
