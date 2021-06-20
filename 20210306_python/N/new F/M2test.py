
n=int(input())
MinV=n
MaxV=n

for i in range (4):
    n=int(input())
    MaxV=max(n,MaxV)
    MinV=min(n,MinV)

print("max={}\nmin={}".format(MaxV,MinV))