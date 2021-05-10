from array import array
import numpy as np
import random as rand
from numpy.core.fromnumeric import reshape
import sys
from numpy.random import randint
ar=np.array([[0,1,2,3,4],[1,2,3,45,6]])
ar2=np.array([1,2,3,4,5])

ar.shape
print(ar.shape) #shape  當array([[0,1,2],[1,2,3]])---->(2,3) 2:框框裡面+兩個框框
                        #當array([0,1,2,3])--->(4,)        框框裡面就是物件
                        #       ([[0],[1,2,3,4,5]])----->(2,) 框框裡面兩個框框,且物件數獨立
#shape若裡面長度一樣，會把物件個數印出來
#長度不一樣，印出有幾個框框(像是幾列)

print(type(ar))#<class 'numpy.ndarray'>

print(ar.dtype)  #如果是長度不一樣的列放在一起，dtype-> "object"
print(ar2.dtype) #長度一樣，看物件是什麽類型的

 
ar2.shape=(1,5)#分成一組 且一組五個物件
aa=ar2.ndim  #看維度
aa=ar2.size  #看元素個數
print(ar2)
print(aa)

'''ar2.shape=(5,1)#分成五組 且一組一個物件共五個
print(ar2)
ar2.shape=(5,) #分成五組 且沒有指定一組幾個物件 故在同一組
print(ar2)'''



print("------------分隔線----------")
a1=np.array([4,8,7,6,3])  #一維

a2=np.array([[4,8,7,6,3],[10,11,12,13,14]]) #二維建立

at=np.arange(1,10)  #從1到n-1

#a3=np.array([(1,2,3,4.5,6.7),(2,3,5,6.6,7.7,8.8)])
#print(a3)

o=np.ones((2,3,3))*128  #可以直接全部運算，不需要再寫迴圈 #宣告單位矩陣，2維 3*3的矩陣 跟matlab一樣
#print(o)

f8=np.full((2,3,3),128)
#print(f8)


rand_np = np.random.rand(2,3,3)  #2維3*3的矩陣，當中為亂數0~1產生
#print(rand_np)   
randint_np = np.random.randint(2,135 ,size=(2,3))  #2~135 int  size 3*3矩陣
print(randint_np)
print("\n")
reshape_np = randint_np.reshape(6)
print(reshape_np)
print("\n")

#氣泡排序法
for i in range(0,len(reshape_np)):
    for j in range(i,len(reshape_np)):
        if reshape_np[i]>reshape_np[j]:
            tmp=reshape_np[i]
            reshape_np[i]=reshape_np[j]
            reshape_np[j]=tmp
print(reshape_np)

#這邊是找中位數， 要注意長度以及list中index的關系 
if len(reshape_np) % 2 ==0: #偶數
    x = reshape_np[len(reshape_np)//2-1] + reshape_np[ len(reshape_np)//2]
    x=x//2

else :
    x=reshape_np[len(reshape_np)//2]
print(x)

fileName="out2,npy"  #設定檔名
with open(fileName,"wb") as fp:  
    np.save(fp,randint_np)  #把亂數矩陣儲存


print("----------------分隔線-----------------")
r=np.random.shuffle(reshape_np)  #使用shuffle可以打亂

print(r)



data=sys.argv[2]
print(data)
rand.seed(int(sys.argv[1]))
rand.shuffle(data)
print("".join(data))  #把list中的引號合併




