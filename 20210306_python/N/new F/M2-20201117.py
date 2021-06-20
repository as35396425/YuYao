n=int(input())
o=''
for i in range(n):
    x,y,z=map(int,input().split())

    if x>=60 and y>=60  and z>=60:  #3個皆60分
        z=('p')
    elif (x>=60 and y>=60) or (x>=60 and z>=60) or (z>=60 and y>=60)   and x+y+z>=220: #有一項沒六十=其他兩項皆60   3個加起來超過220
        z=('P')
    elif (x>=60 and y>=60) or (x>=60 and z>=60) or (y>=60 and z>=60) and (x+y+z)<220: #
        z=('M')
    elif (x<60 and y<60) or(x<60 and z<60) or (y<60 and z<60 )  and (x>=80 or y>=80 or z>=80):
        z=('M')
    else :  
        z=('F')
    o=o+z+'\n'


print(o,end='')
print
#Q7