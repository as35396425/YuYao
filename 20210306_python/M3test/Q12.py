n,m=map(int,input().split())

data1=list(map(int,input().split()))
data2=list(map(int,input().split()))
data3=[]

for i in range(n):
    for j in range(m):
        if data1[i]==data2[j] and data2[j]not in data3:
            data3.append(data2[j])
print(len(data3))
