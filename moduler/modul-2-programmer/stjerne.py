import turtle

# Definerer tre variabler vars verdier brukes til å tegne stjernen
antall_takker = 5
lengde = 200
grader = 180 - 180/ antall_takker

# Løkke som tegner figuren
for i in range(antall_takker):
    turtle.forward(lengde)
    turtle.right(grader)

# Holder på vinduet
turtle.done()
