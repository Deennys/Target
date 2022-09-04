import json

def media(colecao):
    media = 0
    aux = converter(colecao)
    i = 0
    while i < len(aux):
        media += aux[i]
        i+=1
    media /= (len(aux))
    return media
   
def converter(colecao):
    newCo = []
    i = 0
    for e in colecao:
        if e['valor'] > 0:
            newCo.append(e['valor'])
    return newCo

def contadorDeDias(colecao):
    nmDias = 0
    md = media(colecao)
    aux = converter(colecao)
    for e in aux:
        if md < e:
            nmDias += 1
        
    return nmDias


with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

dinheiro = converter(dados)
dias = contadorDeDias(dados)
print("O menor valor de faturamento foi de: R${:.2f}".format(min(dinheiro)))
print("O maior valor de faturamento foi de: R${:.2f}".format(max(dinheiro)))
print("O numero de dias em que o faturamento foi maior que a media foram:", dias, "dias")    

