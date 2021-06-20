def fun1(m,n):
    if m%n==0:
        return n
    else:
        return fun1(n,m%n)

        
m,n=map(int,input().split())
print(fun1(max(m,n),min(m,n)))