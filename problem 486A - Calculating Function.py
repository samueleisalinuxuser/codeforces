def cf(n):
    if n >= 1 and n <= 10**15:
        c = 0

        if n%2 == 0: c = int(n/2)

        else: c = int(n/2)-n

        return c

try: print(cf(int(input())))
except: pass

"""
I noticed that if the number is even, it can be divided in n/2 block -n +(n+1) and the sum of each block is equal to 1.
    For example, if we consider the number 10:
        -1 +2  -3 +4  -5 +6  -7 +8  -9 +10 = +1  +1  +1  +1  +1 = 5

If the number is odd we have to do the same process, but we have to consider the last number which will be subtracted from n/2.
    For example, if we consider the number 15:
        -1 +2  -3 +4  -5 +6  -7 +8  -9 +10  -11 +12 -13 +14  -15 = +1  +1  +1  +1  +1  +1 +1 -15 = +7 -15 = -8
"""
