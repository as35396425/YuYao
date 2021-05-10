# 加密程式的筆記

## 注意事項:

不能給予種子後，在把字串跟索引值一起打亂(shuffle)

種子(seed)每個種子對應不同的亂數表，故有順序之分，index and string會依照不同的亂數被打亂

→會無法推回去(解密)

主要核心概念:

seed和shuffle的關係:

關於加密:

先打亂索引值，再用索引值帶入字串，例如asia a=0 s=1 i=2 a=3 

但被打亂後，val不會變但是index會變，

ex:[0,3,1,2]  strlist=["a","a","s","i"]

```python
rand.shuffle(xd) 
strlist=[]  
for i in range(len(data)):
	strlist.append(data[xd[i]])
```

關於解密:

ex:

已知: [0,3,1,2]  strlist=["a","a","s","i"]

val各有代表的字元

```python
colist=[None]*len(strlist)
for i in range(len(strlist)):
	colist[xd[i]]=strlist[i]  
```

原本加密訊息是aasi→有索引值所以放入colist 且xd[i]與strlist[i]本來就是對照的，

所以依照此放入colist  總而言之就是，[0312]and[aasi]照順序跑，看index放入colist

上面因為要指定給colist，但是設定空的會是沒東西，所以在裡面裝[None]
