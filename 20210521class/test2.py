from PIL import Image , ImageDraw

newImg = Image.new("RGBA",(300,300),"#201377")#RGBA代表有一個alpha層，會有去背效果
   #  井字號後面代表色碼RGB 從00~ff
DOb = ImageDraw.Draw(newImg)#可以把newImg變成一張圖畫紙


for i in range(0,300,1):
        DOb.point([i,i],fill ="red")
        DOb.point([i,300-i],fill ="red")
        DOb.point([150,300-i],fill ="red")
        DOb.point([300-i,150],fill ="red")
for i in range(100,200,1):
    for j in range(100,200,1):

        DOb.point([j,i],fill="black")
        DOb.point([i,j],fill="black")

color = ["#0080FF","#1180FF" ,"#0080FF"]
for i in range(1,10,3):
    DOb.line([(3+i,3+i),(296-i,3+i),(296-i,296-i),(3+i,296-i),(3+i,3+i)],fill = 'white' )



for i in range(150,310,5):  #畫網狀線用的迴圈  #影像處理當中，座標(0,0)在最左上角
    DOb.line([(i,0),(300,i-150)],fill="yellow") #黃色，從座標(i,0)到(300,i-150) 

    DOb.line([(300-i,0),(0,i-150)],fill="red")

    DOb.line([(i-150,300),(0,i)])

    DOb.line([(i,300),(300,450-i)])



  

newImg.save("testIMG.png")#有alpha層，可以儲存為png檔
    