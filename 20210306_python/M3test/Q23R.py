def f(x):
    flag=True
    if x==1:
        flag=False
    for i in range(2,x//2+1):
        if x%i==0:
            flag=False
    return flag

x=int(input())
for i in range(3,x):
    if f(i)==True and f(x-i)==True:
        if x-i>=i:
            print("{}+{}".format(i,x-i))





