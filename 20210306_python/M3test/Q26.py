def fun1(x,y):
    if y ==1:
        return x
    else:
        return x*fun1(x,y-1)


def fun2(x,y):
    if y==1:
        return x
    
    elif y%2==0:
        return fun2(x,y/2)*fun2(x,y/2)

    elif y%2!=0:
        return x*fun2(x,y-1)
    


x,y=map(int,input().split())
print(fun1(x,y))
print(fun2(x,y))