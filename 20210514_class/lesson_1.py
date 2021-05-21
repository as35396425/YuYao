try:
    x=int(input("number:"))  #輸入一個東西 但輸入錯誤 可自訂錯誤內容輸出
except ValueError:
    print("input data error")  #如果輸入錯誤 會印出此訊息
else:
    print(x) #若沒有錯誤，照常輸出


