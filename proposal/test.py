from os import name
import numpy
from numpy.core.fromnumeric import std
import requests
import urllib
from bs4 import BeautifulSoup
import pandas
import matplotlib.pyplot as plt
from scipy.stats import norm
import sys

keyword = input("請輸入關鍵字")
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'x-api-source': 'pc',
    'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}',
    'SPC_SI':'bfftoctw1.gmUO1A7agpvBFRgNtMG2gUW4ZwulVYmf'
} 
 #urllib.parse.quote是編碼過程，可以把漢字轉換成平常看網址看不懂的格式
"""         特殊符号：汉字、&、=等特殊符号编码为%xx          """


s = requests.Session()
url = 'https://shopee.tw/api/v4/search/product_labels'# 去觀察    'SPC_SI':'bfftoctw1.gmUO1A7agpvBFRgNtMG2gUW4ZwulVYmf'
                                                        #搜尋到其中一個值再請求上面的url
r = s.get(url, headers=headers)
r.encoding = "utf8"
base_url = 'https://shopee.tw/api/v4/search/search_items/' #基本頁面  網址若v2 name在items裡面  若v4 name在 items的item_basic裡面

query = f"by=relevancy&categoryids=7904&keyword={keyword}&limit=100&newest=0&order=desc&page_type=search&version=2&page=1"  #不同的值給予不同類型頁面 ex: limit = 10 order=desc
#categoryids=7904 分類顯示卡
url = base_url + '?' + query
r = s.get(url, headers=headers)


if r.status_code == requests.codes.ok:
    data = r.json()
    infom = ""
    D=dict()
    name_list  = []
    price_list = []

    for i in range(len(data["items"])):
        #print(data["items"])
        #break
        name = data["items"][i]["item_basic"]["name"]
        price = int(data["items"][i]["item_basic"]["price"]) // 100000  
        #print("{}:{}".format(name,price))
        outP ="{}:{}".format(name,price)
        #if 40000 > price > 10000:  #考慮到賣家會不合理設價格，先設此if條件
        infom+=outP+'\n'
        D[name] = price
        name_list.append(name)
        price_list.append(price)
            #print(D)

    #print(D)
    data_P = pandas.Series(D)
    data_pandas_frame = pandas.DataFrame({  "name":name_list
                                          , "price":price_list  
                                                                })
    
    xpt = data_pandas_frame.index
    
    ypt = price_list
    plt.hist(data_pandas_frame['price'])
    plt.show()
    plt.scatter(ypt,xpt)
    plt.show()
    print(data_pandas_frame.describe())
    Pdata = numpy.array(data_pandas_frame['price'])
    Pstd =  numpy.std(Pdata)
    Pmean = numpy.mean(Pdata)
        #print(Pstd,Pmean)
    '''產生價格的標準差以及平均數"'''
    #ypt  = norm.pdf(ypt,Pmean,Pstd)
    #plt.plot(price_list,ypt)
    #plt.show()
    #------------------------------------------
    data_pandas_frame.to_csv("sp_out_D","\t",encoding="utf8")
    
    
    '''
    for i in data:
        if i == "items":
            infom.append(data[i])
            
            print(infom)
    '''
    with open('shopee.text', 'w', encoding='utf-8') as f:
        f.write(infom)
