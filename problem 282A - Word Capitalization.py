"""
A. Word Capitalization
time limit per test2 seconds
memory limit per test256 megabytes
input: standard input
output: standard output

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.
Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters.
The length of the word will not exceed 103.

Output
Output the given word after capitalization.

Examples
input
ApPLe
output
ApPLe
input
konjac
output
Konjac
"""

try:
    w,wl = input(),list()

    if len(w) <= 10**3 and " " not in w:
        for i in w: wl.append(i)
    
    del i,w

    wl[0],w = wl[0].capitalize(),""

    for i in wl: w+=i

    print(w)

except: pass
