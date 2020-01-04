# Program som lar brukeren gjette på et tall
from random import randint 

# Variabler for minste og største verdi
min = 1
maks = 10

# Trekker et tilfeldig tall
korrekt_tall = randint(min, maks)

# Løkke som gjentar seg så lenge brukeren ikke har gjettet korrekt
gjettet_korrekt = False
while not gjettet_korrekt:
    gjettning = input(f"Gjett et tall mellom {min} og {maks}: ")
    gjettet_tall = int(gjettning)
    gjettet_korrekt = gjettet_tall == korrekt_tall
    if gjettet_tall < korrekt_tall:
        print(f"{gjettet_tall} er for litet")
    elif gjettet_tall > korrekt_tall:
        print(f"{gjettet_tall} er for stort")
    else:
        print("Du gjettet korrekt!!")
    