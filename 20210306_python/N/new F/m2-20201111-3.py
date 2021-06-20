
n=int(input())
print('{:08b}'.format((n)))
bnStr=""
while n//2>=1:  #如果n//2>=1 就繼續做  因為是二進制 如果<=1 就代表不會進位
    bnStr=str(n%2)+bnStr  #用於更新變數  剩下的餘數+字串
    n=n//2   #更新變數  讓while不會無限loop 
bnStr=str(n)+bnStr  #若出來 str(n)已經小於2不會進入while 故再加上去
print('{:08}'.format(int(bnStr)))  #以八位數 若空格補0 


#十進位轉二進位