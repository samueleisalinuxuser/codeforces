"""
A. Beautiful Year
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.
Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input
The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.

Output
Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct.
It is guaranteed that the answer exists.

Examples
input
1987
output
2013
input
2013
output
2014
"""

def v(y):
    y,ys,cv = str(y),set(),True

    for i in y: ys.add(i)

    """
    I have chosen to convert the given year into a string and to copy the
    values of the string into a set because if the values were equal, only
    one would be inserted into the set and so to verify that the given year
    does not have equal numbers we just need to compare the length of the
    year string and the length of the set with the copied values
    """

    if len(y) == len(ys): return True
    else: return False

try:
    y = int(input())
    if y >= 1000 and y <= 9000:

        if v(y) == True: y+=1
        while v(y) != True: y+=1

        print(y)

except: pass
