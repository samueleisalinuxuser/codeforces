try:
    n = int(input())
    if n >= 1 and n <= 100:

        bf,bfi,fs = ["I hate","I love"],0,""

        for i in range(n):
            fs += bf[bfi]
            
            if bfi == 1: bfi = 0
            else: bfi = 1

            if i != n-1: fs += " that "
            else: fs += " it"
        
        print(fs)

except: pass
