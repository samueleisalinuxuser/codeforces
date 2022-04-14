try:
    p = input()

    if len(p) >= 1 and len(p) <= 100:
        v = True
        
        for i in p:
            if ord(i) < 33 or ord(i) > 126:
                v = False
                break
            else: continue
        
        if v == True:
            if "H" in p or "Q" in p or "9" in p: print("YES")
            else: print("NO")

except: pass
