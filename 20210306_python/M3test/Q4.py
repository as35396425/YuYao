def fun(w,h):
    for i in range(1,h+1):
        for j in range(1,w+1):
            print("{}\t".format(i*j),end="")
        print()

w,h=map(int,input().split())
(fun(w,h))