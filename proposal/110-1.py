import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://mcma.asia.edu.tw/zh_tw/faculty"

r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")


tag_table = soup.find(attrs={"class":"l-content--2col--main l-container jobs-content"})  # 找到<table>
ALL_Professors = tag_table.find_all("div",class_="b-block__left")
csvfile = "110_104.CSV"

with open(csvfile, 'w+', newline='', encoding="utf8") as fp:
    writer = csv.writer(fp)
    OneRecordDict = {"職稱":"","公司":"","Place":"","經歷":"","Degree":""}
    OneRecordDict_Map = {"職稱":"職稱","公司":"公司","Place":"Place","經歷":"經歷","Degree":"Degree"}
            
    for onefield in OneRecordDict.keys():
            fp.write(OneRecordDict_Map[onefield]+',')
    fp.write('\n')
    

    for One in ALL_Professors: #每次處理一列訊息
        OneRecordList = []
        OneRecordDict = {"職稱":"","公司":"","Place":"","經歷":"","Degree":""}
    
        NameInfStr = One.find('a').text.replace('  ','')
        OneRecordDict["職稱"] = NameInfStr
        OneRecordList.append(NameInfStr) #名字
        print(NameInfStr)

        lil = One.find_all("li",class_="b-list-inline b-clearfix") #其他資料
        for oneItem in lil: #每次處理一列的訊息 
            title = oneItem.find('li','b-list-inline b-clearfix')
            value = oneItem.find('li','b-list-inline b-clearfix')
                
"""

            if (title.text.find("學歷") >= 0 ):
                OneRecordDict["Degree"] = value.text #學歷訊息


            if (title.text.find("研究室") >= 0 ):
                Location = value.text #辦公室位置訊息
                if (Location.find('大樓') != -1):
                    BuildName = Location[:Location.find('大樓')]
                    OneRecordDict["Building"] = BuildName+'大樓'
                    OneRecordDict['辦公室'] = Location[Location.rfind('樓')+1:]
                else:
                    OneRecordDict['辦公室'] = Location
                    if (Location.find('I') != -1):
                        OneRecordDict["Building"] = '資訊大樓'
                    elif (Location.find('H')!= -1):
                        OneRecordDict["Building"] = '健康大樓'
                    elif (Location.find('M')!= -1):
                        OneRecordDict["Building"] = '管理大樓'
                    else:
                        OneRecordDict["Building"] = ''

            if (title.text.find("學校分機") >= 0 ):
                OneRecordDict["分機"] = value.text #分機訊息

            if (title.text.find("職稱") >= 0 ):
                OneRecordDict["職稱"] = value.text #職稱訊息

            if (title.text.find("專長") >= 0 ):
                OneRecordDict["研究"] = value.text.replace(',','、') #研究訊息
                
            if (oneItem.find('a') != None):
                OneRecordDict["E-mail"]=oneItem.find('a').text

        for onefield in OneRecordDict.keys():
            fp.write(OneRecordDict[onefield]+',')
            
        fp.write('\n')       
"""