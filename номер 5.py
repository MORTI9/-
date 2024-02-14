fin=open("space (1).txt","r",encoding="utf-8")
title = fin.readline()
spa=[x.strip().split("*") for x in fin]
d = {}
def hash_pl(st):

    global d
    if st[1]in d:
        d[st[1]]+=","+st[0]
    else:
        d[st[1]]=st[0]
    return d
for x in spa:
    hash_pl(x)
k=0
for x in spa:
    print("Ключ "+x[1]+" значение "+d[str(x[1])])
    k+=1
    if k==10:
        break


