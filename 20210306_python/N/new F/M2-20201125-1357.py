n=int(input())
v1=1
v2=1
if n == 1:
    print(v1)
elif n==2:
    print("{}\t{}".format(v1,v2))
else:
    print("{}\t{}".format(v1,v2),end='')  #\t tab寬度的字元
    for i in range (n-2):
        print("\t{}".format(v1+v2),end='')   #\t如果在進來不會跑上面的條件 所以先輸出前面(1,1)的數字
        v3=v1+v2   #先設定一個v3變數 紀錄v1+v2
        v1=v2      #指定v2給v1    
        v2=v3      #指定相加過後的數字給v2
#1 1 2 3 5 8 13 21  費式數列
#數列方式為Fn= Fn-1+Fn-2(n>=2時)
#ex 3 為1+2  5為2+3  