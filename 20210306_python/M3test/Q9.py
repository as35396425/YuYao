data=list(map(int,input().split()))

for i in range(len(data)):
    for j in range(i,len(data)):
        if data[i]>data[j]:
            tmp=data[i]
            data[i]=data[j]
            data[j]=tmp

for i in data:
    print("{} ".format(i),end="")
