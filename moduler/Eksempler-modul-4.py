# Kode 4.1
print("Anna kjøper for: {} kr".format(2*15 + 32 + 2*34 + 78))
print("Else kjøper for: {} kr".format(2*32 + 34 + 2*78))


# Kode 4.2
melk = 15
brød = 32
smør = 34
ost = 78
print("Anna kjøper for: {} kr".format(2*melk + brød + 2*smør + ost))
print("Else kjøper for: {} kr".format(2*brød + smør + 2*ost))


# Kode 4.3
melk = 12
smør = 30
print("Anna kjøper for: {} kr".format(2*melk + brød + 2*smør + ost))
print("Else kjøper for: {} kr".format(2*brød + smør + 2*ost))

# Kode 4.4
navn = input("Hva heter du: ")
print("Hei {}! Håper du liker mitt program!".format(navn))

# Kode 4.5
melk = 15
brød = 32
navn = input("Hva heter du: ")
antall_melk = int(input("Hvor mange liter melk vil du ha {}: ".format(navn)))
antall_brød = int(input("Hvor mange brød vil du ha {}: ".format(navn)))
pris = antall_brød*brød + antall_melk*melk
print("Takk for kjøpet {}. Du kjøpte {} brød og {} melk for: {} kr".format( 
          navn, antall_brød, antall_melk, pris))

