import requests
from bs4 import BeautifulSoup

req = requests.get("http://isrc.ccs.asia.edu.tw/www/myjournal/myjournal.htm")
req.encoding="big5"
if req.status_code== 200:

    #print(req.text)
    soup=BeautifulSoup(req.text,"lxml")#抓資料時要看哪個是標的物(EX:ul=沒有序列 li="list item" ol="oder list" class="")

    result1=soup.find_all("span",lang='EN-US' )   #find_all 找到全部 若用find只能找1個 找<li> 
    fp=open("outtwo.txt","w",encoding="utf8")  #open (檔名，寫入模式，編碼)
    for val in result1:
        text2=val.text.replace("\n","")   #將錯誤的字變成空白
        print(text2)
        fp.write(text2+"\n")  #寫資料到記憶體 記得要關才會寫成檔案()<span style='mso-tab-count:1'>
    fp.close()
else:
    print("no page")

#1.get URL 200為有回應 404=error  2.用BeautifulSoup把.text--->lxml  3.
