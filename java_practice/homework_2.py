h={
   "tom":[80 , 100 , 90 , 95],"jhon":[100,93,75,80]
  }
avg_T=h["tom"]
avg_j = h["jhon"]


'''
x = 0
count=0

for i in avg_T:
    x+=i
    count+=1

avg_T=x//count
print(avg_T)

'''


print("Tom的平均:{}".format(sum(avg_T)//len(avg_T)))
print("Jhon的平均:{}".format(sum(avg_j)//len(avg_j)))