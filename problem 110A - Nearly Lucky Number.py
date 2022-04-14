try:
    n = int(input())
    if n >= 1 and n <= 10**18:

        lns = str(n).count("4") + str(n).count("7")
        if lns == 4 or lns == 7: print("YES")
        else: print("NO")

except: pass
