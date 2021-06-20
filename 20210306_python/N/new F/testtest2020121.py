n=int(input())
flag = True
for i in range (2,n//2+1):
    if n%i == 0:
        flag = False
        break
if flag == True :
    print('yes')
else :
    print('NO')

    #質數判別