n=int(input())
x=0
for i in range(2,n+1):
    tmp=i
    while tmp%2==0:
        tmp//=2
    while tmp%3==0:
        tmp//=3
    while tmp %5==0:
        tmp//=5
    if tmp==1:
        x+=i
print(x)


