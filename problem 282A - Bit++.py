try:
    n = int(input())
    if n >= 1 and n <= 150:
        s,x,c = [],0,True
        
        for i in range(n):
            s = input()

            if s in ["++x","x++","++X","X++"]: x+=1
            elif s in ["--x","x--","--X","X--"]: x-=1
            else:
                c = False
                break
        
        if c == True: print(x)

except: pass
