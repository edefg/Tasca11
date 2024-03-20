def pos(p):
    r = [x**p for x in range(1,10)]
    print("Les potencies elevades a {} dels 10 primers numeors es {}".format(p,r))

p = int(input("Intrudueix un numero al  qual voleu elevar la resta: "))
pos(p)
