'''
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
'''

#自己寫的解法
def namelist(names):
    l = []
    c=0
    string = ""

    for i in names:
        l.append(i)

        if c == len(names)-1:
            string += str(l[c]['name'])  #因為是包在list裡面，所以先指定list的index 再指定dict的key
        elif c == len(names)-2:
            string += str(l[c]['name'])+" & "
        else:
            string += str(l[c]['name'])+", "

        c+=1
    
    return string

#參考解法1
def namelist(names):
    if len(names) > 1:          #到 -1 等於到最後一個之前(部會把最後一個加進去)，加進去name  name的型態會是({name:人名})，再指定key且用join加入到 ", "
                                #format'{}'這是最後一個之前，當中包括逗號
                                #第二個{}指定index為最後一個，也是指定key format進去 
                                #思路是分開成前面跟最後一個，中間加&符號  逗號則是前面就加完
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), #可以使用join來代替用for迴圈的用法，
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''
    
    
        
        
        