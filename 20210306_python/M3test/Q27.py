def fun(x):
    if x>=10:
        return 1+fun(x//10)
    else:
        return 1


x=int(input())
print(fun(x))