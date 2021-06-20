idi={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'X':10}

data=list((input().split()))

arr1=[]
x=0
for i in data:
    x+=idi[i]
    arr1.append(x)
x=0
for i in arr1:
    x+=i
if x%11==0:
    print("YES")
else:
    print("NO")