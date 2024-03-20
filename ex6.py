def coicideixin(llista):
    l = []
    for i, e in enumerate(llista):
        if e ==i:
            l.append(e)
    print("Els elements de la llista {} que consideixen en la posicio son {}".format(llista, l))

#pp
l = [3,7,2,3,4,5,6,7,8,9,10,11]
coicideixin(l)
