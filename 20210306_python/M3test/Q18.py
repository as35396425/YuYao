n=int(input())
x1=[]
for i in range(n):
    x=list(input().split())
    data=[0]*len(x)
    for i in range(len(x)):
        if x[i][0]=="C":
            data[i]=0
        elif x[i][0]=="D":
            data[i]=13      
        elif x[i][0]=="H":
            data[i]=26
        elif x[i][0]=="S":
            data[i]=39 
        data[i]+=int(x[i][1:])
    
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if data[i]<data[j]:
                tmp=data[i]
                data[i]=data[j]
                data[j]=tmp
                
                tmp=x[i]
                x[i]=x[j]
                x[j]=tmp
    x1.append(x)


print(x1)
