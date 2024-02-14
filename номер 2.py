fin=open("space (1).txt","r",encoding="utf-8")
title = fin.readline()
spa=[x.strip().split("*") for x in fin]
"""for x in spa:
    n=x[0][-3:]
    print(n)"""
for i in range(1,len(spa)):
    for j in range(i,0,-1):
        if spa[j][0][-3:]<spa[j-1][0][-3:]:
            spa[j],spa[j-1]=spa[j-1],spa[j]

k=0
for x in spa:
    print(x[1])
    k+=1
    if k==10:
        break