data=[]
for i in range(5):
    data.append((input().split()))

for i in range(7):
    for j in range(5):
        print("{}\t".format(data[j][i]),end='')
    print() 