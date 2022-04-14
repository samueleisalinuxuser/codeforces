try:
    n = int(input())
    if n>= 1 and n<= 100:
        for i in range(n):
        
            w = input()
        
            if len(w) > 10 and w.islower() == True:
                print(w[0]+str(len(w)-2)+w[-1])

            else: print(w)

except: pass
