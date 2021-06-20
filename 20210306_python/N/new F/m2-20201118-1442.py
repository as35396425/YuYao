n=int(input())
sum1=0
i=0
while n%10 ==0:
    n=n//10
    i=i+1
while n %10 >0:  #若n無法被10整除
    sum1=sum1+(n%10)
    n=n//10
    i=i+1
print(i)
print(sum1)
#M2 Q17數字串和  輸出 幾位數 和 總和 
