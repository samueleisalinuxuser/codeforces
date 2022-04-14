try:
    k,n,w = input().split(" ")
    k,n,w = int(k),int(n),int(w)

    if k >= 1 and w <= 1000 and n >= 0 and n <= 10**9:

        tc = k*sum(list(range(1,w+1)))

        if n >= tc: print(0)
        else: print(tc-n)

except: pass
