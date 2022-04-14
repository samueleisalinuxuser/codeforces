try:
    n,k = list(int(i) for i in input().split(" "))

    if n >= 2 and n <= 10**9 and k >= 1 and k <= 50:
        
        for i in range(k):
            if str(n)[-1] != "0": n-=1
            
            elif str(n)[-1] == "0": n = int(n/10)

        print(n)

except: pass
