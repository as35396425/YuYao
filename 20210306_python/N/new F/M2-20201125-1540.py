n=int(input())
sum1=1
for i in range (2,n+1):  
    sum1=sum1+i  #連續加整數
    if sum1==n:
        print(i)
        break
    if sum1>n:
        print(i-1)
        break
    #Q24