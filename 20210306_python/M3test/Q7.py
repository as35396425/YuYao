n=int(input())
data=[]
for i in range(n):
    data.append(int(input()))

for i in range(len(data)):
    for j in range(i+1,len(data)):
        if data[i]>data[j]:
            tmp=data[i]
            data[i]=data[j]
            data[j]=tmp

for i in data:
    print(i)