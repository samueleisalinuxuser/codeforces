try:
    a,b = list(int(i) for i in input().split(" "))

    if a >= 1 and b >= 1 and b >= a and a <= 10 and b <= 10:

        y = 0

        while a <= b:
            a*=3
            b*=2
            y+=1
        
        print(y)
        
except: pass
