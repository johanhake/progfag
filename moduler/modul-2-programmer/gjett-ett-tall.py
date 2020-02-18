from random import randint 
 
# Variabler for minste og største verdi
min = 1
maks = 10
 
# Trekker et tilfeldig tall
korrekt_tall = randint(min, maks)
 
# Løkke som gjentar seg så lenge brukeren ikke har gjettet korrekt
gjettet_tall = min - 1
while gjettet_tall != korrekt_tall:
    gjettet_tall = int(input("Gjett et tall mellom {} og {}: ".format(min, maks)))
    if gjettet_tall < korrekt_tall:
        print("{} er for litet".format(gjettet_tall))
    elif gjettet_tall > korrekt_tall:
        print("{} er for stort".format(gjettet_tall))
    else:
        print("Du gjettet korrekt!!")
