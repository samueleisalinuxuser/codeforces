try:
    n = int(input())
    if n >= 1 and n <= 100000:
        s,v = input(),True

        if len(s) == n:

            for i in s:
                if i not in ["A","D"]:
                    v = False
                    break
        
            if v == True:

                if s.count("A") > s.count("D"): print("Anton")
                elif s.count("D") > s.count("A"): print("Danik")
                elif s.count("A") == s.count("D"): print("Friendship")

except: pass
