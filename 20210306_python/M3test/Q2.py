import random
key=int(input())
random.seed(key)

data=[0]*6
i=0
while i<6:
    x=random.randint(1,43)
    flag=True
    j=0
    while j<i and flag==True:
        if data[j]==x:
            flag=False
        j+=1
    if flag==True:
        data[i]=x
        i+=1

for j in data:
    print("{}\t".format(j),end="")
print()
