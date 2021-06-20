class Student:
    def __init__(self,name,cl,ID,home,gender):
        self.name=name
        self.Cl=cl
        self.ID=ID
        self.Home=home 
        self.Gender=gender

    def showinfo(self):
        print(self.name,end=" ")
        print(self.Cl,end=" ")
        print(self.ID,end=" ")
        print(self.Home,end=" ")
        print(self.Gender,end=" ")
        print()


x1=Student("楊于曜","資工系","109021490","高雄市岡山區","男")
x2=Student("Kirito","刀劍系","109048763","艾恩葛朗特22層","女")
x3=Student("asuna","公共運輸系","108084687","艾恩葛朗特22層","男")

x1.showinfo()
x2.showinfo()
x3.showinfo()
