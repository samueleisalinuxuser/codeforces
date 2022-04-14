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
