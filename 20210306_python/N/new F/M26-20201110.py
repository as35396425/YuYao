n=int(input())
for i in range(1,n):
    for k in range (n-i-1):
        print(' ',end='')    
    for j in range(2*i-1):
        print('*',end='')

    print() 


for r in range(1,n):
    for z in range(r):
        print(' ',end='')
    for l in range (2*(n-r)-3):
        print('*',end='')

    print()