try:
    n,t = input(),input()
    if len(n) > 0 and len(n) <= 100 and n.isupper() == False and len(t) > 0 and len(t) <= 100 and t.isupper() == False:
        if n == t[::-1]: print("YES")
        else: print("NO")

except: pass
