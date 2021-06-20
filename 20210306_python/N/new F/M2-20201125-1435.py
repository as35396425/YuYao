n=int(input())

for j in range (2,n+1): #跑要列出來的數字
    flag=True
    for i in range (2,j//2+1):#比較快 且跑出除掉的數
        if j%i==0:
            flag=False
            break
    if flag==True:
        print(j)

        #質數不會被自己以外的數字整除
        #Q20 質數列表