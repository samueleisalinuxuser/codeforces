import random
from random import choice

ps = 0

try:
    n = int(input())

    if n>=1 and n<=1000:

        for i in range(n):

            pb = input()

            try:
                p,v,t = pb.split(" ")
                p,v,t = int(p), int(v), int(t)

                if p in range(2) and v in range(2) and t in range(2):
                    s = p+v+t

                    if s == 3 or s == 2: ps+=1
        
            except: pass
except: pass

print(ps)
