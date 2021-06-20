#
# Jing-Doo Wang
# jdwang@asia.edu.tw
# 2020.5.21
#

import requests
from bs4 import BeautifulSoup
import csv

#url = "https://www.w3schools.com/html/html_media.asp"
url = "https://csie3.asia.edu.tw/faculty/professors"

r = requests.get(url)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
#print (soup.text)
#print (soup)
#print (soup.prettify())


#tag_table = soup.div(class_="w3-table-all")  # 找到<table>
# class="row contact-category"
#tag_table = soup.find(class_="row contact-category")  # 找到<table>
tag_table = soup.find(attrs={"class":"row contact-category"})  # 找到<table>
#print (tag_table)
#print (tag_table.prettify())

# <div class="col-sm-12">
ALL_Professors = tag_table.find_all("div",class_="col-sm-12")
#print(ALL_Professors[0])
#print(ALL_Professors[0].text)
#print(ALL_Professors[1])
#print(ALL_Professors[1].text)

# 開啟CSV檔案寫入截取的資料

#csvfile = "AU_CSIE_Professor_jdwang2020_5_20_UTF8.csv"
#csvfile = "AU_CSIE_Professor_jdwang2020_5_20_BIG5.csv"
csvfile = "AU_CSIE_Professor_jdwang2020_6_4_BIG5_FieldName_Dictionary.csv"


#with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
with open(csvfile, 'w+', newline='', encoding="big5") as fp:
    writer = csv.writer(fp)
    
    Fieldnames = ["姓名","學歷","辦公室","分機","E-mail"]
    writer.writerow(Fieldnames)
    #for row in rows:
    for One in ALL_Professors:
        OneRecordList = []
        OneRecordDict = {"姓名":"","學歷":"","辦公室":"","分機":"","E-mail":""}
        #print (One)
        #print (One.text)
        #####################################################
        #<h2 class="card-header">蔡進發 （Jeffrey J.P. Tsai）</h2>
        #print (One.find('h2','card-header'))
        print (One.find('h2','card-header').string)
        OneRecordDict["姓名"] = One.find('h2','card-header').string
        OneRecordList.append(One.find('h2','card-header').string)   
        #####################################################
        #class="<p class='card-description selectorgadget_rejected'"
        #print (One.find('p','card-description selectorgadget_rejected').string)
        #print (One.find('p','card-description').string)
        #print (One.find('p','card-description').text)
        #print (One.find('p','card-description').text.split()[0])
        #print (One.find('p','card-description').text.split()[1])
        #####################################################
        #ALL_card_description = One.find("p",class_="card-description")
        #ALL_card_description = One.find('p',attrs={"class":"card-description"})       
        #print (ALL_card_description)
        #print (ALL_card_description.text)
        #print (ALL_card_description.text.split()[0])
        #print (ALL_card_description.text.split()[1])
        #####################################################
        ALL_card_description = One.find_all("p",class_="card-description")
        #print (ALL_card_description)
        #print (ALL_card_description[0].text)
        #print (ALL_card_description[0].text.split('：')[0])
        #print (ALL_card_description[0].text.split('：')[1])
        for oneItem in ALL_card_description:
            print (oneItem.text.split('：')[0])
            print (oneItem.text.split('：')[1])
            #print (oneItem.text.split('：')[0].replace("\n",""))
            #OneRecordList.append(oneItem.text.split('：')[1])
            #OneRecordList.append(oneItem.text.split('：')[1].replace("\t",""))
            #OneRecordList.append(oneItem.text.split('：')[1].replace("\t","").replace(" ",""))
            #OneRecordDict[oneItem.text.split('：')[0]] = oneItem.text.split('：')[1].replace("\t","").replace(" ","")
            OneRecordDict[oneItem.text.split('：')[0].replace("\n","")] = oneItem.text.split('：')[1].replace("\t","").replace(" ","")   
        #print(OneRecordList)
        #writer.writerow(OneRecordList)
        print(OneRecordDict)
            
       
       

