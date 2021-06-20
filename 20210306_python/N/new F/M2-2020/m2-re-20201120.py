n=int(input())

for a in range (n):
    for c in range (n-1):
        print(' ',end='')
    for b in range (1):
        print('|',end='')
    print()
       



for i in range(1,n):

    for k in range(i-1):
        print(' ',end='')
    for j in range((2*(n-i)+1)):   #控制他為奇數 利用2n-1 之後設N就好  N=(n+1)-i (n+1)結尾 i為迴圈變數
        print('*',end='')
    print()
for i in range(1,n):
    
    for k in range(i-1):
        print(' ',end='')
    for j in range((2*(n-i)+1)):   #控制他為奇數 利用2n-1 之後設N就好  N=(n+1)-i (n+1)結尾 i為迴圈變數
        print('*',end='')
    print()
for i in range(n):
    
    for k in range(i):
        print(' ',end='')
    for j in range(2*(n-i)-1):   #控制他為奇數 利用2n-1 之後設N就好  N=(n+1)-i (n+1)結尾 i為迴圈變數
        print('*',end='')

    print()
