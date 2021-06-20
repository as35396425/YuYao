class Book:
    def __init__(self,name,year,category,author,language):
        self.name=name
        self.year=year
        self.category=category
        self.author=author
        self.language=language

    def showinfo(self):
        print(self.name,end=" ")
        print(self.year,end=" ")
        print(self.category,end=" ")
        print(self.author,end=" ")
        print(self.language,end=" ")
        print()

x1=Book("無職轉生","2012","異世界輕小說","不講理不求人","日文")
x2=Book("悲慘世界","1862","社會寫實長篇小說","維克多.雨果","法文")
x3=Book("儒林外史","清代","章回長篇諷刺小說","吳敬梓","中文")


x1.showinfo()
x2.showinfo()
x3.showinfo()
