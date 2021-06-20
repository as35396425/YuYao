class Chess:
    def __init__(self,name,color,walk,river,limit):
        self.name=name
        self.C=color
        self.W=walk
        self.R=river
        self.L=limit

    def showinfo(self):
        print(self.name,end=" ")
        print(self.C,end=" ")
        print(self.W,end=" ")
        print(self.R,end=" ")
        print(self.L,end=" ")
        print()


x1=Chess("馬","紅","日字","可過河","無限制")
x2=Chess("將","黑","一格","不可過河","九宮格")
x3=Chess("車","紅","直排","可過河","無限制")

x1.showinfo()
x2.showinfo()
x3.showinfo()
