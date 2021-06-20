n=int(input())
data=list(map(int,input().split()))

for i in range(n):
    os=str(data[i])+" "
    x=data[i]
    for j in range(i+1,n):
        x+=data[j]
        os+=str(data[j])+" "
        if x==0:
            print(os)


       