

import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.104.com.tw/jobs/search/?ro=0&keyword=big%20data&kwop=7&mode=s&jobsource=2018indexpoc"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
          'Referer': 'https://www.104.com.tw/jobs/search/?ro=0&keyword=big%20data&kwop=7&mode=s&jobsource=2018indexpoc', 
          'Connection': 'keep-alive',
                                        }   
r = requests.get(url,headers=header)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")

tag_table = soup.find(attrs={"class":"l-content--2col--main l-container jobs-content"})  # 找到<table>

ALL_Professors = tag_table.find_all("div",class_="b-block__left")

csvfile = "109021086_end.csv"

with open(csvfile, 'w+', newline='', encoding="utf8") as fp:
    writer = csv.writer(fp)
    
    Fieldnames = ["職稱","公司","Place","經歷","Degree"]
    writer.writerow(Fieldnames)

    for One in ALL_Professors:
        OneRecordList = []
        OneRecordDict = {"職稱":"","公司":"","Place":"","經歷":"","Degree":""}
        a = One.find(class_="b-list-inline b-clearfix") #抓取指定tag
        
        
        if a == None:  #排除掉抓到Nonetype
            pass #跟玩牌一樣pass
        else :
            
            #print(a.text.replace("\n","").split("\t"))#如果有none就不能這樣指定.text   可以設想None.text只能抓空氣
            a= a.a
            print(a) #沒有寫產業 只是因為當初企業就沒設定
            print("-------------",(One.find(class_="b-list-inline b-clearfix")))
            OneRecordDict["職稱"] = One.find(class_="b-list-inline b-clearfix")
            OneRecordDict["職稱"] = OneRecordDict["職稱"].find('a')
            print(OneRecordDict["職稱"]["title"])
            ''' 
            find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果.

            find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None .
            '''



        '''
        print(OneRecordDict)        
        OneRecordList.append(One.find(class_="b-list-inline b-clearfix").string)

        ALL_card_description = One.find_all(class_="js-job-link")

        for oneItem in ALL_card_description:
            print (oneItem.text.split('：')[0])
            print (oneItem.text.split('：')[1])

            OneRecordDict[oneItem.text.split('：')[0].replace("\n","")] = oneItem.text.split('：')[1].replace("\t","").replace(" ","")   

        print(OneRecordDict)
        '''
       