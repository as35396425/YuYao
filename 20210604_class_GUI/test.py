
#設定畫布
backG = Canvas(windos,width=450,height=300)  #新增一個畫布物件 寬450高300
img = tk.PhotoImage(file="img.gif")  #畫布只能用gif檔
backG.create_image(250,280,image=img)  #250 280 為偏移值，依照給定的座標進行圖片的偏移
backG.pack(side="left",fill="x",expand=1)
