try:
    n,ar = int(input()),0
    if n >= 1 and n <= 100:
        for i in range(n):
            p,q = input().split(" ")
            p,q = int(p),int(q)
            if p >= 0 and q >= 0 and q >= p and p <= 100 and q <= 100:
                if q-p >= 2: ar+=1
    
    print(ar)

except: pass
