n=int(input())

data=list(map(int,input().split()))
maxv=-99999999999
for i in range(n):
    x=data[i]
    for j in range(i+1,n):
        x*=data[j]
        if x>maxv:
            maxv=x


print(maxv)