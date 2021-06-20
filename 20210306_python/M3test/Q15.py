r1,c1,r2,c2=map(int,input().split())

arr1=[]
arr2=[]
arr3=[[0]*c2 for i in range(r1)]
for i in range(r1):
    arr1.append(list(map(int,input().split())))
for i in range(r2):
    arr2.append(list(map(int,input().split())))

print(arr1,arr2)

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            arr3[i][j]+=arr1[i][k]*arr2[k][j]
print(arr3)
