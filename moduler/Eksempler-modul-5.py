# Kode 5.1
lest = int(input("Hvor mange sider har klassen lest i gjennomsnitt: "))
medalje = 800
if lest >= medalje:
    print("Gratulerer! Klassen får en medalje!")
else:
    print("Klassen får dessverre ikke noen medalje...")

# Kode 5.2
lest = int(input("Hvor mange medaljer har klassen lest i gjennomsnitt: "))
bronse = 800
søll = 1200
gull = 1600
if lest >= gull:
    print("Gratulerer! Klassen får en gullmedalje!")
elif lest >= søll:
    print("Gratulerer! Klassen får en søllmedalje!")
elif lest >= bronse:
    print("Gratulerer! Klassen får en søllmedalje!")
else:
    print("Klassen får dessverre ikke noen medalje...")

# Kode 5.3
alder = int(input("Hva er alderen din: "))
barn = 4
voksen = 16
honnør = 63
if alder < barn:
    pris = 0
elif barn <= alder and alder < honnør:
    pris = 30
else:
    pris = 15
 
print("Prisen for din billett er {} kr".format(pris))

# Kode 5.4
grense = 50
tall = int(input("Skriv et partall som er større enn {}: ".format(grense)))
if tall % 2 == 0 and tall > grense:
    print("{} er et partall og større enn {} :D".format(tall, grense))
else:
    print("{} er ikke et partall eller så er det mindre enn {} :("
          .format(tall, grense))

# Kode 5.5
from random import randint
min = 1
maks = 5
tilfeldig = randint(min, maks)
gjetting = int(input("Gjett et tall mellom {} og {}: ".format(min, maks)))
if gjetting == tilfeldig:
    print("Gratulerer! Du gjettet riktig :D")
else:
    print("Du gjettet dessverre feil :( Riktig svar var {}.".format(tilfeldig))
