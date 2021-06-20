n=int(input())
for i in range (3,n+1):
    for j in range (1,n+1):
        for k in range (1,n+1):
            if k**2== i**2+j**2 and i<=j<=k and (i+j+k<=n):
                print("{}\t{}\t{}".format(i,j,k))




