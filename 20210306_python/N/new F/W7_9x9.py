n=int(input())


for x in range(1,n+1):
    print()
    for y in range(1,n+1):
        print('{:^5d}'.format(x*y),end='')
        