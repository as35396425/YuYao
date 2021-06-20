def sum1(x):
    if x>10:
        return x%10+sum1(x//10)  #舉例1234   4+sum1(123)                 #這邊的函式 把各個位數加起來
    else :
        return x
n=int(input())
data=list(map(int,input().split()))
d=[]
for i in data:
    d.append(sum1(i))

for i in range(n):
    for j in range(i,n):
        if d[i]>d[j]:
            tmp=d[i]
            d[i]=d[j]
            d[j]=tmp

            tmp=data[i]
            data[i]=data[j]
            data[j]=tmp              
        elif (d[i]==d[j]) and data[i]>data[j] :
            tmp=data[i]
            data[i]=data[j]
            data[j]=tmp              

for i in data:
    print(i,end="\t")
