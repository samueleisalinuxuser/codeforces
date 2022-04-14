try:
    un = input()
    if len(un) > 0 and len(un) <= 100 and un.islower() == True:
        
        dc = list()

        for i in un:
            if i not in dc: dc.append(i)

        del i
        
        if len(dc)%2 == 0: print("CHAT WITH HER!")

        else: print("IGNORE HIM!")

except: pass
