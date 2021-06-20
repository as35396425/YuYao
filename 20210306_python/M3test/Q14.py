n=int(input())

arr1=[[0]*n for i in range(n)]
arr2=[[0]*n for i in range(n)]

x=1
for i in range(n):
    if i % 2 ==0:
        for j in range(n):
            arr1[i][j]=x
            arr2[j][i]=x
            x+=1
    if i%2 !=0:
        for j in range(n-1,-1,-1):
            arr1[i][j]=x
            arr2[j][i]=x
            x+=1

for i in range(n):
    for j in range(n):
        print(arr1[i][j],end="\t")
    print()
print()
for i in range(n):
    for j in range(n):
        print(arr2[i][j],end="\t")
    print()
