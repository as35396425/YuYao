x=int(input())
y=list(map(int,input().split()))
print(y)

start=[]
stop=[]

for i in range(0,len(y)):
    if 0<= y[i] <= 24 and 1<= x <= 30 :
        if i%2==0:
            start.append(y[i])
        else:
            stop.append(y[i])


driver = 1
for j in range(0,len(stop)):
    if start[j]>stop[j]   :
        print("錯誤")
        
    elif j+1 < (len(stop)-1):
        if stop[j] > start[j+1]:
            driver += 1

print(start,stop)

print(driver)
    