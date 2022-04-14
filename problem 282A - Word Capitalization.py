try:
    w,wl = input(),list()

    if len(w) <= 10**3 and " " not in w:
        for i in w: wl.append(i)
    
    del i,w

    wl[0],w = wl[0].capitalize(),""

    for i in wl: w+=i

    print(w)

except: pass
