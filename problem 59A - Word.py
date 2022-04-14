try:
    s = input()
    if len(s) >= 1 and len(s) <= 100:

        lcc,ucc = 0,0

        for i in s:
            if i.isupper() == True: ucc+=1
            else: lcc+=1
        
        if lcc >= ucc: s = s.lower()
        else: s = s.upper()
    
        print(s)

except: pass
