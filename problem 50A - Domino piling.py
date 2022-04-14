try:
    m,n = [int(i) for i in input().split(" ")]

    if m >= 1 and m >= 1 and n >= m and m <= 16 and n <= 16:
        print(int(m*n//2))

except: pass
