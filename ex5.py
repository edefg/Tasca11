def crear_diccionari(llista):
    dic = {}
    for i, e in enumerate (llista):
        dic[e]=i
    print("De la llista {} hem creat el diccionari {}".format(llista, dic))

#pp
llista = ["Cotxe", "Casa", "Vaixell", "Columna", "Ca", "Mussol", "Clara"]
crear_diccionari(llista)