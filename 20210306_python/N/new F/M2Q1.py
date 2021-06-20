n=int(input())
maxVal=int()
for i in range(n):
    y=int(input())
    maxVal=max(maxVal,y)      #找一個數可判斷最大值(上面的0)然後儲存最大值 進入下個迴圈
print('max={}'.format(maxVal))


