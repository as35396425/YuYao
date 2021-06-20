y,m=map(int,input().split())
data=[31,28,31,30,31,30,31,31,30,31,30,31]
STD=y//4+y//400-y//100
TD=STD*366+(y-STD)*365
print(TD)
flag=False
if y%4==0:
    flag=True
elif y%100==0:
    flag=False
elif y%400==0:
    flag=True
if flag==True:
    data[1]=29
x=1
c=0
for i in range(m-1):
    TD+=data[i]
    print(TD)
startD=TD%7
su=["SU","MO","TU","WE","TH","FR","SA"] #設定星期幾
for i in range(7):  
    print(su[i],end="\t") 
print()

for i in range(startD):
    print("\t",end="")
    c+=1
for j in range(data[m-1]):
    print(x,end="\t")
    c+=1
    x+=1
    if c%7==0:
        print()

    

