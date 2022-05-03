import random

number = range(1,14)
naipe = ["Paus", "Copas", "Espadas", "Ouros"]
lista_v =[]
lista_ai=[]

for i in range(0,3):
    noice = random.choice(naipe)
    numero = (random.choice(number))
    if numero > 10:
        if numero == 11:
            numero = "Dama"
        elif numero == 12:
            numero = "Valete"
        elif numero == 13:
            numero = "Rei"
    elif numero == 1:
        numero = "Ás"
    str : str(numero)
    mão = (f"{numero} de {noice}")
    lista_v.append(mão)
    
for i in range(0,3):
    noice = random.choice(naipe)
    numero = (random.choice(number))
    if numero > 10:
        if numero == 11:
            numero = "Dama"
        elif numero == 12:
            numero = "Valete"
        elif numero == 13:
            numero = "Rei"
    elif numero == 1:
        numero = "Ás"
    str : str(numero)
    mão = (f"{numero} de {noice}")
    lista_ai.append(mão)
