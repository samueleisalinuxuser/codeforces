try:
    n = int(input())
    if n >= 1 and n <= 100:
        """
        As the problem says the string contains a letter of the latin alphabet
        if this letter occurs in the string in uppercase or lowercase, the program
        change all the letters in the string in lowercase, than it converts the string
        in a set as to delete all duplicates.
        """
        s = set(input().lower())

        """
        Finally, the program checks if the lenght of the set is equal to the lenght of the
        latin alphabet and it prints the correct output.
        """
        if len(s) == 26: print("YES") #The latin alphabeth contains 26 letters.
        else: print("NO")

except: pass
