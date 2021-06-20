# 課堂練習測試
    1.python
    課堂練習使用markdown編輯檔案
<img src="https://media.discordapp.net/attachments/772481237511569420/819809032750628874/unknown.png?width=1004&height=565" >

<font face="標楷體" color="#008600">
<h2 style="background:black">以上為示範圖片</h2>
</font>
<br>
<br>

# whit is object
    State <---->Behavior
    ex 腳踏車

    屬性: 比方說"人":name high weight  color.etc
    behavior : sleep eating fighting ---> in 程式 叫做function
    
    ex: puppy
    data member : name color breed hungry
    function member :barking fetching .....
    object 都有自己的status


# Class in PY
    def ----> 定義function 
    定義class----> 有自己的namespeace
    first charcter 寫成大寫 若沒有 會被人誤為涵式
    (之前在java上看到的Scanner 可能為如此)

    global and local 
    
    global:
    local:



# Class PY 2
    __init__()  給物件初始的東西
    init= initial




    class Student:
    def __init__(self,name,id):
        self.STUname=name  #把name 給 self.STUname
        self.STUid=id      #把id 給 self.id



    x= Student("楊于曜","109021490")  #設定基本狀態
    print(x.STUname , x.STUid)


    #簡單的物件導向
    
    #概念:先設定給class基本狀態 or 在設定好名字的櫃子拿東西出來用
    
# Class in py 3 
    __dict__ 
    __doc__  用來印備註 若無則不做
    __base__ 可以繼承制某個類別 EX:學生:姓名身高體重 系所 ID
                                  老師:姓名身高體重 系所
                                  職員:姓名身高體重 單位
    有許多一樣的狀態，直接一起繼承下來，有點類似css語法
    在java中 唯一繼承而已 但是有介面的觀念 python則無介面之觀念
    有點類似大家都會走路，但是有不同特殊技能

    作業: 定義--->showinfo() 之函式 呈現人物資料，

# 檔案說明 
    In respositories  檔案以語言 時間命名
    
    較早兩個是課堂練習

    較晚兩個是回家功課





