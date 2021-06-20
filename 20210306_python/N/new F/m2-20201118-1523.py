n=int(input())

for i in range (1,n//2+1):
    outStr= ''
    sum1=0 ; j=i 
    while sum1<n:  #迴圈跑的總和超過n 就不進入迴圈 進到下面的判斷式
        if j==i:  #確保第一個數前面不會有'+'
            outStr=str(j)
            sum1=sum1+j
            j+=1   #迴圈跑幾次
        else:
            outStr=outStr+'+'+str(j)  #將連續整數以字串型態累加
            sum1=sum1+j             #同時 int型態也計算
            j+=1
    if sum1 == n :  #如果上面加起來有等於n 則print出紀錄字串
        print(outStr)
if sum1 !=n:
    print('no')


#M2 Q18 尋找連續整數相加 