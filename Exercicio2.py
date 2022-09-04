def checarFibonacci(n): 
    priDig = 0
    segDig = 1
    pos = 1
    while n != priDig and n > priDig :
        aux = priDig + segDig
        priDig = segDig
        segDig = aux
        pos += 1
    if n == priDig :
        if priDig == 1 :
            return print("O numero 1 esta presente na segunda e na terceira posição de Fibonacci.")
        return print(f"O numero {n} esta presente na {pos}º posição de Fibonacci.")
    return print("O numero", n, "não esta na sequencia de Fibonacci.")


num = int(input("Digite o numero que deseja consultar na sequencia de Fibonacci: "))
checarFibonacci(num)