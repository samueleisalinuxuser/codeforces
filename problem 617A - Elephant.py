try:
    x,m = int(input()),0
    if x >= 1 and x <= 1000000:

        for i in range(5,0,-1):

            while x >= i:
                x-=i
                m+=1
             
        print(m)

except: pass
