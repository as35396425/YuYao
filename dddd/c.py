w,h  = map(int,input("輸入身高與重量").split())

bmi = w/(h/100)**2
if bmi<18.5:
    print("過輕")
elif 18.5 <= bmi < 24:
    print("正常範圍")   
elif 24<=bmi<=27:
    print("過重")
elif 27<=bmi<=30:
    print("輕度肥胖")
elif 30<=bmi<35:
    print("中度肥胖")
elif bmi>=35:
    print("重度肥胖")
    