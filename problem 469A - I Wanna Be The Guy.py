"""
A. I Wanna Be the Guy
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

There is a game called "I Wanna Be the Guy", consisting of n levels. Little X and his friend Little Y are addicted to the game.
Each of them wants to pass the whole game.
Little X can pass only p levels of the game. And Little Y can pass only q levels of the game.
You are given the indices of levels Little X can pass and the indices of levels Little Y can pass.
Will Little X and Little Y pass the whole game, if they cooperate each other?

Input
The first line contains a single integer n (1 ≤ n ≤ 100).
The next line contains an integer p (0 ≤ p ≤ n) at first, then follows p distinct integers a1, a2, ..., ap (1 ≤ ai ≤ n). These integers denote the indices of levels Little X can pass.
The next line contains the levels Little Y can pass in the same format. It's assumed that levels are numbered from 1 to n.

Output
If they can pass all the levels, print "I become the guy.". If it's impossible, print "Oh, my keyboard!" (without the quotes).

Examples
input
4
3 1 2 3
2 2 4
output
I become the guy.
input
4
3 1 2 3
2 2 3
output
Oh, my keyboard!

Note
In the first sample, Little X can pass levels [1 2 3], and Little Y can pass level [2 4], so they can pass all the levels both.
In the second sample, no one can pass level 4.
"""

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