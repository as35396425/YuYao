def fun(x):
    z=1
    for i in range(x,1,-1):
        z=z*i
    return z


m,n=map(int,input().split())

print(fun(m)//(fun(n)*fun(m-n)))

