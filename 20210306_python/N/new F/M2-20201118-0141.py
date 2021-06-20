a,b=map(int,input().split())
x=max(a,b)
y=min(a,b)
while x%y>0:  #如果x/y之餘數大於0 就繼續做
    tmp=x%y  #儲存餘數在tmp
    x=y  #將最小值指定給x
    y=tmp #將x/y之餘數 指定給y
print(y)
print(int(a*b/y))

#輾轉相除法   兩個數對除  再用兩數之最小值除於兩數之餘數