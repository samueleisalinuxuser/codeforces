try:
    n = int(input())
    if n >= 1 and n <= 100000:
        ms = [input() for i in range(n)]

        v = True
        for i in ms:
            if i not in ["01","10"]:
                v = False
                break
        del i

        if v == True:
            g,pm = 1,ms[0]
            for i in ms[1:]:
                if i == pm[::-1]:
                    g+=1
                    pm = i
            
            print(g)

except: pass
