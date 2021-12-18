def verificarExpressao(expressao):
    pilha = []
    for paranteses in expressao:
        if paranteses =='(':
            pilha.append('aberto')
        else:
            pilha.append('fechado')

    abertos = 0
    fechados = 0
    for x in pilha:
        if x == 'aberto':
            abertos += 1
        else:
            fechados +=1
    
    if abertos == fechados:
        print(expressao + ' - OK')
    else:
        print(expressao + ' - ERRO')


expressao1 = "(())"
expressao2 = "()()(()())"
expressao3 = "())"

verificarExpressao(expressao1)
verificarExpressao(expressao2)
verificarExpressao(expressao3)


