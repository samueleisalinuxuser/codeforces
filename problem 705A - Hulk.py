"""
A. Hulk
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Dr. Bruce Banner hates his enemies (like others don't). As we all know, he can barely talk when he turns into the incredible Hulk.
That's why he asked you to help him to express his feelings.
Hulk likes the Inception so much, and like that his feelings are complicated. They have n layers.
The first layer is hate, second one is love, third one is hate and so on...
For example if n = 1, then his feeling is "I hate it" or if n = 2 it's "I hate that I love it", and if n = 3 it's "I hate that I love that I hate it" and so on.
Please help Dr. Banner.

Input
The only line of the input contains a single integer n (1 ≤ n ≤ 100) — the number of layers of love and hate.

Output
Print Dr.Banner's feeling in one line.

Examples
input
1
output
I hate it
input
2
output
I hate that I love it
inputCopy
3
output
I hate that I love that I hate it
"""

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
