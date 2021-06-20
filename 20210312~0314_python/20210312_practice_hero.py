class Hero:
    def __init__(self,name,ID,atk,defn,speed):
        self.Hname=name
        self.ID=ID
        self.Hatk=atk
        self.Hdefn=defn
        self.speed=speed

    def showinfo(self):
        print(self.Hname)
        print(self.ID)
        print(self.Hatk)
        print(self.Hdefn)
        print(self.speed)



x1=Hero("小火龍","004","52","43","65")
x2=Hero("妙蛙種子","001","49","49","45")
x3=Hero("傑尼龜","007","49","65","43")

x1.showinfo()
x2.showinfo()
x3.showinfo()
