"""
A. Translation
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

The translation from the Berland language into the Birland language is not an easy task.
Those languages are very similar: a berlandish word differs from a birlandish word with the same meaning a little: it is spelled (and pronounced) reversely.
For example, a Berlandish word code corresponds to a Birlandish word edoc. However, it's easy to make a mistake during the «translation».
Vasya translated word s from Berlandish into Birlandish as t.
Help him: find out if he translated the word correctly.

Input
The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters.
The input data do not consist unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

Output
If the word t is a word s, written reversely, print YES, otherwise print NO.

Examples
input
code
edoc
output
YES
input
abb
aba
output
NO
input
code
code
output
NO
"""

try:
    n,t = input(),input()
    if len(n) > 0 and len(n) <= 100 and n.isupper() == False and len(t) > 0 and len(t) <= 100 and t.isupper() == False:
        if n == t[::-1]: print("YES")
        else: print("NO")

except: pass