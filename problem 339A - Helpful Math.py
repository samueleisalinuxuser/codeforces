"""
A. Helpful Maths
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.
The teacher has written down the sum of multiple numbers.
Pupils should calculate the sum. To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia.
She is only beginning to count, so she can calculate a sum only if the summands follow in non-decreasing order.
For example, she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.
You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces.
It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3.
String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.

Examples
input
3+2+1
output
1+2+3
input
1+1+3+1+3
output
1+1+1+3+3
input
2
output
2
"""

try:
    c,oc,ns = input().split("+"),list(),""
    
    if "1" in c or "2" in c or "3" in c:
        if len(c) > 1:

            n = 1

            for i in range(3):
                for ii in range(c.count(str(n))):

                    oc.append(str(n))
                    oc.append("+")

                n+=1
            
            del i

            for i in oc[:-1]: ns+=i

            print(ns)
        
        else: print(c[0]) 

except: pass