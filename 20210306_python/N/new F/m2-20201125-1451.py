n=int(input())
y=1
for i in range (n,1,-1):
    y=y*i
x=0
while y % 10 ==0:
    y=y//10
    x=x+1

print(x)

#Q21