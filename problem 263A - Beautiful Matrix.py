try:
    m = [input().split(" ") for i in range(5)]

    v,no,nz,ro,co = True,0,0,0,0

    for i in m:
        if len(i) == 5:
            if "0" in i or "1" in i:
                if i.count("1") == 1:

                    ro,co = m.index(i),i.index("1")

                    no+=1
                    nz+=4
                    
                elif i.count("0") == 5: nz+=5

                else:
                    v = False
                    break
        
        else:
            v = False
            break
    
    del i
        
    if no != 1 or nz != 24: v = False

    if v == True:
        m = 0

        if ro == co == 2: m = 0

        else:
            m+=abs(2-ro)
            m+=abs(2-co)

        print(m)

except: pass
