"""
A. Calculating Function
time limit per test1 second
memory limit per test256 megabytes
input: standard input
output: standard output

For a positive integer n let's define a function f:
f(n) =  - 1 + 2 - 3 + .. + ( - 1)**n*n
Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 10**15).

Output
Print f(n) in a single line.

Examples
input
4
output
2
input
5
output
-3

Note
f(4) =  - 1 + 2 - 3 + 4 = 2
f(5) =  - 1 + 2 - 3 + 4 - 5 = -3
"""

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
