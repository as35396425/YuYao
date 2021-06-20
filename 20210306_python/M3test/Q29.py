def fun(x):
    if x==0:
        return x
    elif x==1:
        return x
    else:
        return fun(x-1)+fun(x-2)

print(fun(int(input())))
