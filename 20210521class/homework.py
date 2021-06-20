from os import sep
import sys
from PIL import Image
from PIL import ImageFilter
from glob import glob

def Menu():
    print("=============================")
    print("1:等比縮放")
    print("2:圖片旋轉")
    print("3:產生縮圖")
    print("4:套用濾鏡")
    print("7:格式轉換(指定)")
    print("8:格式轉換(全部) 之後會改 統一改成未輸入做批次 ")
    print("0:結束")
    print("可指定檔名使用以上效果，若無則批次處理")
    print("=============================")



def getfilter(imgname):
    
    print("=============================")
    print("1:模糊")
    print("2:輪廓")
    print("3:細節增強")
    print("4:邊緣增強")
    print("5:深度邊緣增強")
    print("6:浮雕效果")
    print("7:邊緣訊息")
    print('8:平滑效果')
    print('9:深度平滑效果')
    print("A.:銳利化效果")
    print("0:結束")
    op = input("選擇功能:")
    print("===============================")
    if type(imgname) == str:
        imgname=[imgname]

    for img_0 in imgname:
        img = Image.open(img_0)
        if op=="1":
            img.filter(ImageFilter.BLUR)#模糊
            str1 = "模糊效果"
        elif op=="2":
            img.filter(ImageFilter.CONTOUR)
            str1 = "輪廓"
        elif op=="3":
            img.filter(ImageFilter.DETAIL)
            str1 = "細節增強"
        elif op=="4":
            img.filter(ImageFilter.EDGE_ENHANCE)
            str1 = "邊緣增強"
        elif op=="5":
            img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            str1 = "深度邊緣增強"
        elif op=="6":
            img.filter(ImageFilter.EMBOSS)
            str1 = "浮雕效果"
        elif op=="7":
            img.filter(ImageFilter.FIND_EDGES)
            str1 = "邊緣訊息"
        elif op=="8":
            img.filter(ImageFilter.SMOOTH)
            str1 = "平滑效果"
        elif op=="9":
            img.filter(ImageFilter.SMOOTH_MORE)
            str1 = "深度平滑效果"
        elif op=="A":
            img.filter(ImageFilter.SHARPEN)
            str1 = "銳利化效果"
        dotIndex = img_0.index(".")
        #print(dotIndex)#顯示點的位置
        newImgname = img_0[:dotIndex] + str1 + img_0[dotIndex:]
        #print(newImgname)#顯示名字
        img.save(newImgname)
        print("{}濾鏡以儲存".format(str1),newImgname,"\n")

def resizeImg(imgname):
    try:
        
        img = Image.open(imgname)
        print("size(width,height):",img.size)
        new_w=int(input("new_width:"))
        ratio = float(new_w)/img.size[0]# 新寬度  / index 0  原始寬度
        new_h = int(img.size[1]*ratio)#index 1 為原始高度，在乘上倍率
        resizedImg = img.resize((new_w,new_h),Image.BILINEAR)  #BICUBIC 效果較漂亮
        print("newImage_size:",resizedImg.size)
        dotIndex = imgname.index(".")
        print(dotIndex)
        newImgname = imgname[:dotIndex]+"_resized"+imgname[dotIndex:]
        print(newImgname)
        resizedImg.save(newImgname)
        print("resized圖片以儲存",newImgname,"\n")

    except FileNotFoundError as fnfe:
        print(fnfe)

def rotateImg(imgname):
    try:
        print("選項")
        print("1:左右")
        print("2:上下")
        print("3:90")
        print("4:180")
        print("5:270")
        print('6:other')
        op_1 = input("請輸入選項")
        if type(imgname) == str:
            imgname=[imgname]

        for img_0 in imgname:
            img = Image.open(img_0)
            if op_1 == '1':
                newI = img.transpose(Image.FLIP_LEFT_RIGHT)
            elif op_1 == '2':
                newI = img.transpose(Image.FLIP_TOP_BOTTOM)
            elif op_1 == "3":
                newI = img.transpose(Image.ROTATE_90)
            elif op_1 == '4':
                newI = img.transpose(Image.ROTATE_180)
            elif op_1 == "5":
                newI = img.transpose(Image.ROTATE_270)
            elif op_1 =="6":
                deg = float(input("輸入角度:"))
                newI = img.rotate(deg)

            dotIndex = img_0.index(".")
        #print(dotIndex)
            newImgname = img_0[:dotIndex]+"_RO"+img_0[dotIndex:]
            print(newImgname)
            newI.save(newImgname)
            print("rotate圖片以儲存",newImgname,"\n")

    except FileNotFoundError as fnfe:
        print("沒有存")

def jpg2png(imgname):
    try:
        im = Image.open(imgname)

        dotIndex = imgname.index(".")
        newImgname = imgname[:dotIndex]+"_notsame"+".png"
        im.save(newImgname)  # im.save(new_name,"png")  後面不用指定副檔名沒關係，程式將會自動判斷副檔名
        print("轉換完成")

    except FileNotFoundError as fnfe:
        print(fnfe)
        
def png2jpg(imgname):
    try:
        im = Image.open(imgname)
        im = im.convert("RGB")  #需先轉換為RGB格式  因為PNG為rgba的檔案格式之一，可是jpg不是

        dotIndex = imgname.index(".")
        newImgname = imgname[:dotIndex]+"_notsame"+".jpg"
        im.save(newImgname)  #im.save(new_name,"jpg")  與上面同理
        print("轉換完成")
    except FileNotFoundError as fnfe:
        print(fnfe)



def getT(imgname):
    try:
        if type(imgname) == str:
            imgname=[imgname]
        
        new_w , new_h = map(int,input("輸入變更的寬高 : ").split())
        for img_0 in imgname:
            img = Image.open(img_0)
            print("size(width,height):",img.size,"\n")
            img.thumbnail((new_w,new_h))  #要兩個括號，也就是說放在同一個變數當中
            dotIndex = img_0.index(".")
            #print(dotIndex)
            newImgname = img_0[:dotIndex]+"_thumbnail"+img_0[dotIndex:]
            print(newImgname)
            img.save(newImgname)
            print("thumbnail圖片以儲存",newImgname,"\n")    

    except FileNotFoundError as fnfe:
        print(fnfe)

if __name__ == "__main__":
    if len (sys.argv)>=1:
        Menu()
        op = input("選擇功能")
        if op == "1":
            if len(sys.argv)>1: #如果有指定檔名 --->縮放
                resizeImg(sys.argv[1])
            elif len(sys.argv) == 1:  #沒有指定，也就是沒有給參數
                print("要進行批次嗎?")  
                ch = input("Yes/No")  #選單功能
                if ch == "Yes":   #yes 
                    x = input("jpg/png : ") #選檔案格式
                    if  x == 'jpg':
                        imList = glob("*.[jJ][pP][gG]")  #會製作成list
                        rotateImg(imList)
                        print(imList)
                        print("處理完成")
                
                    elif   x == "png":
                        imList = glob("*.[pP][nN][gG]") #會製作成list
                        rotateImg(imList)
                        print(imList)
                        print("處理完成")
        
        if op == "2":
            if len(sys.argv)>1:
                rotateImg(sys.argv[1])
            else:
                x=input("要進行批次嗎?\nyes or no \n請輸入 : ")
                if x == "yes":
                    x = input("jpg/png")
                    if  x == 'jpg':
                        imList = glob("*.[jJ][pP][gG]")
                        rotateImg(imList)
                        print(*imList,sep="")
                        print("處理完成")
                
                    elif   x == "png":
                        imList = glob("*.[pP][nN][gG]")
                        
                        rotateImg(imList)
                        print(imList)
                        print("處理完成")

        
        if op == "3":
            if len(sys.argv)>1:
                getT(sys.argv[1])
                print("產生縮圖")
            else:
                x=input("要進行批次嗎? \n yes or no \n 請輸入 : ")
                if x == "yes":
                    x = input("請選擇 jpg/png :")
                    if  x == 'jpg':
                        imList = glob("*.[jJ][pP][gG]")
                        getT(imList)
                        print(*imList,sep="")
                        print("處理完成")
                    elif   x == "png":
                        imList = glob("*.[pP][nN][gG]")
                        getT(imList)
                        print(*imList,sep="")
                        print("處理完成")
        if op == "4":
            if len(sys.argv)>1:
                getfilter(sys.argv[1])
            else:
                x=input("要進行批次嗎? \n yes or no \n 請輸入 : ")
                if x == "yes":
                    x = input("請選擇 : jpg/png ")
                    if  x == 'jpg':
                        imList = glob("*.[jJ][pP][gG]")
                        getfilter(imList)
                        print(*imList,sep="")
                        print("處理完成")

                    elif   x == "png":
                        iimList = glob("*.[pP][nN][gG]")
                        getfilter(imList)
                        print(*imList,sep="")
                        print("處理完成")
        if op == "7":
            if(sys.argv[1][-3:]) == "jpg":
                jpg2png(sys.argv[1])
                print("jpg to png")
            
            elif(sys.argv[1][-3:]) == "png":
                png2jpg(sys.argv[1])
                print("png to jpg")
            else:
                print("錯誤")
        if op == '8':
            print("1:png to jpg")
            print("2:jpg to png")
            op_1 = int(input("選擇:"))
            if op_1 == 1:
                imList = glob("*.[pP][nN][gG]")
                for imgname in imList:
                    print(imgname)
                    png2jpg(imgname)
            
            elif op_1 == 2:
                imList = glob("*.[jJ][pP][gG]")
                for imgname in imList:
                    print(imgname)
                    jpg2png(imgname)

        if op == "0":
            print("================")
            print("一切都結束了嗎?")
            print("================")
    else:
        print("error")