fin=open("space (1).txt","r",encoding="utf-8")
title = fin.readline().strip()
spa=[x.strip().split("*") for x in fin]
for x in spa:
    pos1=x[1][-3:]
    cent=x[0][1:3]
    cent=cent[::-1]
    perv=x[1][0:3]
    perv=perv[::-1]
    parol=pos1+cent+perv
    parol=parol.upper()
    x+=[parol]
fout=open("space_uniq_password.csv","w",encoding="utf-8")
fout.write(title+"*"+"password"+"\n")
for x in spa:
    print(x)
    fout.write("*".join(x)+"\n")