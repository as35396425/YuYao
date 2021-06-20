n=list((input()))
d=dict()

for i in n:
    if i in d.keys():
        d[i]+=1
    elif i!=' ':
        d[i]=1

for i in sorted(d):
    print("{}={}".format(i,str(d[i])))
