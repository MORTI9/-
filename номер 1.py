fin=open("space.txt","r",encoding="utf-8")
title = fin.readline()
spa=[x.strip().split("*") for x in fin]
for x in spa:
    nol=x[2].split()
    if nol[0]=="0" and nol[1]=="0":
        n=x[0][5]
        m=x[0][6]
        t=len(x[1])
        xd=(x[3].split())[0]
        yd=(x[3].split())[1]
        if int(n)>5:
            xk=str(int(n)+int(xd))
        else:
            xk=str(-(int(n)+int(xd))*4+t)
        if int(m)>3:
            yk=str(int(m)+t+int(yd))
        else:
            yk=str(-(int(n)+int(yd)*int(m)))
        x[2]=f'{xk} {yk}'
fout=open("space_new.txt","w",encoding="utf-8")
fout.write(title)
for x in spa:
    if x[0][3]=="V":
        print(f"{x[0]} - {x[2]}")
    fout.write("*".join(x)+"\n")





