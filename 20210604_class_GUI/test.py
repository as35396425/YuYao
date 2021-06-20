'''
#設定畫布
backG = Canvas(windos,width=450,height=300)  #新增一個畫布物件 寬450高300
img = tk.PhotoImage(file="img.gif")  #畫布只能用gif檔
backG.create_image(250,280,image=img)  #250 280 為偏移值，依照給定的座標進行圖片的偏移
backG.pack(side="left",fill="x",expand=1)
'''
# x="157"
# y=3
# print(x[0:-1])

import hashlib


d= {
    
    
    'sha256':{      
                "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4" : '1234',
                '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8' :"password",
                'bef57ec7f53a6d40beb640a780a639c83bc29ac8a9816f1fc6c5c6dcd93c4721' :"abcdef",
                "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5" :"qwerty"
                
                
                },
    "sha1":{
        
        "1be168ff837f043bde17c0314341c84271047b31" : "1234"   ,
        "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8":"password" ,
        "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2":"abcdef"   ,
        "b1b3773a05c0ed0176787a4f1574ff0075f7521e":"qwerty"   ,
            
            
            },
    "md5":{
        
        "81dc9bdb52d04dc20036dbd8313ed055" : "1234"   ,
        "5f4dcc3b5aa765d61d8327deb882cf99":"password" ,
        "e80b5017098950fc58aad83c8c14978e":"abcdef"   ,
        "d8578edf8458ce06fbc5bb76a58c5ca4":"qwerty"   ,   
            }
    }





x=str(input())


def s256(x):
    h256 = hashlib.sha256()
    h256.update(x.encode("utf8"))
    h256 = h256.hexdigest()
    print(h256)
    return h256

def md5(x):
    m5 = hashlib.md5()
    m5.update(x.encode("utf8"))
    m5 = m5.hexdigest()
    print(m5)
    return m5

def s1(x):
    h1 = hashlib.sha1()
    h1.update(x.encode("utf8"))
    h1 = h1.hexdigest()
    print(h1)
    return h1


outP=""

for i in d:
    for j in d[i]:
        #print(j ,d[i][j])
        
        if x == j:
            outP = "{}方法加密 原始數據:{}".format(i,d[i][j])
            print(outP)

if outP == "":
    print("不在加密庫")
    d["sha256"][s256(x)]=x
    d["sha1"][s256(x)]=x
    d["md5"][s256(x)]=x




