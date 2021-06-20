import requests
from bs4 import BeautifulSoup

req = requests.get("http://dns2.asia.edu.tw/~jdwang/PaperList.htm")
req.encoding="big5"
if req.status_code== 200:

    #print(req.text)
    soup=BeautifulSoup(req.text,"lxml")#抓資料時要看哪個是標的物(EX:ul=沒有序列 li="list item" ol="oder list" class="")
    i=1
    result1=soup.find_all("li" )   #find_all 找到全部 若用find只能找1個 找<li> 
    fp=open("outtwos.txt","w",encoding="utf8")  #open (檔名，寫入模式，寫入編碼)
    for val in result1:
        text2=val.text.replace("\n","")
        print(text2)
        fp.write(str(i)+"  "+text2+"\n")  #寫資料到記憶體 記得要關才會寫成檔案()<span style='mso-tab-count:1'>
        i+=1
    fp.close()
else:
    print("no page")


