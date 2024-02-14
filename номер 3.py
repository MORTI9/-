fin=open("space (1).txt","r",encoding="utf-8")
title = fin.readline()
spa=[x.strip().split("*") for x in fin]
while True:
    n=input("Назавание корабля ")
    if n.upper()=="STOP":
        break
    for x in spa:
        if n==x[0]:
            print(f"Корабль {x[0]} был отправлен с планеты {x[1]} и его направление было {x[3]}")
            break
    else:
        print("error.. er.. ror..")