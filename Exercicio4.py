def total(colecao):
    total = 0
    i = 1
    while i < len(colecao):
        total += colecao[i]
        i += 2
    return total

def participacao(colecao):
    aux = []
    i = 1
    while i < len(colecao):
        aux.append(colecao[i-1])
        aux.append(colecao[i] * 100 / total(colecao))
        i += 2
    return aux

def Formatado(colecao):
    txtFormat = ""
    i = 0
    while i < len(colecao):
        txtFormat += colecao[i] + ": {:.2f}% \n".format(float(colecao[i+1]))
        i += 2
    return txtFormat    

conjunto = ("SP", 67836.43, "RJ", 36678.66, "MG", 29229.88, "ES", 27165.48, "Outros", 19849.53)
conjuntoPor = participacao(conjunto)
resultado = Formatado(conjuntoPor)
print(resultado)