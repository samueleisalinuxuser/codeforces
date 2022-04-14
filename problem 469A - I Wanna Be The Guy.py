try:
    n = int(input())
    if n >= 1 and n <= 100:

        p,q = [int(i) for i in input().split(" ")],[int(i) for i in input().split(" ")]

        def c(l):
            global n
            
            v = True

            if l[0] >= 0 and l[0] <= n:
                for i in l[1:]:
                    if i < 1 and i > n:
                        v = False
                        break
                    
            else: v = False

            return v

        if c(p) == c(q) == True:
            if p[0] == len(p)-1 and q[0] == len(q)-1 and list(set(p[1:]+q[1:])) == list(range(1,n+1)): print("I become the guy.")
                
            else: print("Oh, my keyboard!")

except: pass
