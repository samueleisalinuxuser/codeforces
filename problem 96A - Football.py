try:
    ps = input()

    if len(ps) <= 100 and "1":
        v = True

        for i in ps:
            if i not in ["0","1"]:
                v = False
                break
        
        if v == True:
            if 7*"0" in ps or 7*"1" in ps: print("YES")
            else: print("NO")

except: pass
