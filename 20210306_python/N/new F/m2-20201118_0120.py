n=int(input())
flag = True  #先假設flag是質數
for i in range (2,n//2+1):  #質數從二開始 整除二為提升速度,且不會整除到自己,且自己附近不太可能整除自己
    if n%i == 0:  # 如果可以被整除  那就判斷為質數
        flag = False
        break  #迴圈破壞 不做了
if flag ==True :
    print('yes')
else :
    print('NO')

    #質數判別   