def inverter(palavra):
    i = 0
    invertida = ''
    while i < len(palavra):
        if i > 0:
            invertida += palavra[-i]
        i += 1
    invertida += palavra[0]
    return invertida

plvr = input("Digite a palavra ou frase que deseja inverter: ")
result = inverter(plvr)
print(result)

    