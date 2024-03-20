def lenp(frase):
    r = frase.split(" ")
    l = list(map(len, r))
    print("La longitut de la paraula de la frase {} es {}".format(frase, l))

frase = input("Esciu una frase: ")
lenp(frase)