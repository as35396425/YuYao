from glob import glob
import sys
from PIL import Image
'''
try:
    x=int(input("number:"))  #輸入一個東西 但輸入錯誤 可自訂錯誤內容輸出
except ValueError:
    print("input data error")  #如果輸入錯誤 會印出此訊息
else:
    print(x) #若沒有錯誤，照常輸出
'''

def jpg2png(old_name,new_name):
    try:
        im = Image.open(old_name)
        im.save(new_name)  # im.save(new_name,"png")  後面不用指定副檔名沒關係，程式將會自動判斷副檔名
    except FileNotFoundError as fnfe:
        print(fnfe)
        
def png2jpg(old_name,new_name):
    try:
        im = Image.open(old_name)
        im = im.convert("RGB")  #需先轉換為RGB格式  因為PNG為rgba的檔案格式之一，可是jpg不是
        im.save(new_name,)  #im.save(new_name,"jpg")  與上面同理
    except FileNotFoundError as fnfe:
        print(fnfe)



if __name__ == "__main__":
    if len(sys.argv)>1:
        if sys.argv[1] == "-jpg2png":#條件取決於做什麼動作
            imList = glob("*.[jJ][pP][gG]")#尋找有幾個附屬檔名為jpg的，並加進去list

            #所有的用星號 後面為附屬檔名
            #在微軟的作業系統當中，副檔名大小寫不分
            #使用正規語言表示法(regular expression)
            for imgname in imList:#把檔案夾內抓到的檔案做成的list，一一指定給imgname
                jpg2png(imgname,imgname[:-3]+"png")#imgname[:-3]不需要副檔名，只需要本來的檔案名稱，附屬檔名再另外指定png
            #print(imList)#印出來
        elif sys.argv[1] == "-png2jpg":
            imList = glob("*.[pP][nN][gG]")
            print(imList)
        

