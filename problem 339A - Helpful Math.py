try:
    c,oc,ns = input().split("+"),list(),""
    
    if "1" in c or "2" in c or "3" in c:
        if len(c) > 1:

            n = 1

            for i in range(3):
                for ii in range(c.count(str(n))):

                    oc.append(str(n))
                    oc.append("+")

                n+=1
            
            del i

            for i in oc[:-1]: ns+=i

            print(ns)
        
        else: print(c[0]) 

except: pass
