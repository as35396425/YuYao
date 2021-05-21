import numpy as np
from PIL import Image
from numpy import asarray
from matplotlib import pyplot as plt

n=[
    [100,150,30],
    [30,155,20],
    [101,10,20]
            ]
n=np.array(n)
In=Image.fromarray(n)
plt.imshow(In)
plt.show()
print(n[1][2])
t=[[0]*3]*3
#t=np.array(t) 需先變成np
for i in range(len(n)):
    for j in range(len(n[1])):
        t[i][j]=100+n[i][j]
        print(t)

print("變成np前的list:t\n{}".format(t))
#可從上面看出，將np指定給list，會變成每個高都一起變
It=Image.fromarray(t)
plt.imshow(It)
plt.show()



