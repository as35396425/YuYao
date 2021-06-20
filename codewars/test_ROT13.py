def rot13(message,arr=[] ,a=""):
    for i in range(len(message)):
        if 65 <= ord(message[i]) <= 90:
            x=ord(message[i])+13 
            while x >90:
                x=x-26
            arr.append(chr(x))
            

        elif 97 <= ord(message[i]) <= 122:
            x=ord(message[i])+13 
            while x >122:
                x=x-26
            arr.append(chr(x))
            
        else:
            arr.append(message[i])
        
    for i in arr:
        a=a+i
    
    return a
