x,y=map(int,input().split())
c=0
for i in range(x,y+1):
    if i%2 != 0:
        c=c+i
        print(c)


