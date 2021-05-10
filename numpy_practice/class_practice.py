import sys
import random as rand 
import numpy as np
if __name__ == "__main__":
    if len (sys.argv)>2:
        seedval = int(sys.argv[1])  #取得第一輸入   
        data = list(sys.argv[2])   #第二輸入
        rand.seed(seedval)  #seedval為亂數的種子
        xd=(np.arange(0,len(data)))  #產生一個依照0~輸入資料之長度的數列
        rand.shuffle(xd) #打亂資料  -> 索引值
        strlist=[]  #設定一個空list  用途在於 亂數產生的索引值帶入字串，再添加進去此list
        for i in range(len(data)):
            strlist.append(data[xd[i]])  
        print("".join(data))
        print(xd)
        print(strlist)
    print("-------分隔線------  ")

    x=input("yes or no:")
    if x=="yes":
        colist=[None]*len(strlist)
        for i in range(len(strlist)):
            colist[xd[i]]=strlist[i]  #使用亂數產生的list當作索引值，看索引值把strlist依序放入colist
        print(colist)
    else:
        print('不進行解碼')

    print("-----------分隔線------------")

#how to do decode
