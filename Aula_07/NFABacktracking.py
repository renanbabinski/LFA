# Configuração do Autômato
#############################

aceitacao = {2}
estado_inicial = 0

#estados 0,1,2,...
#alfabeto 0,1

transicao = [[[0,1], [0]],
             [[],    [2]],
             [[],    []]]

entrada = input("Digite a entrada\n")
#############################


def testa(entrada, estados, posicao):
    if posicao == len(entrada):
        # só para mostrar a última configuração instantânea antes do backtracking
        imprimeCI(entrada, estados[0], posicao)
        if aceita(estados):
            return estados
        print("<<backtrack>> Fim da cadeia")
        return None
    
    elemento = int(entrada[posicao])
    for i in estados:
        imprimeCI(entrada, i, posicao)
        novos_estados = transicao[i][elemento]
        if(len(novos_estados) == 0):
            #imprimeCI(entrada, novos_estados[0], posicao)
            print("<<backtracking>> Sem opções")
            return None
        transicoes = testa(entrada, novos_estados, posicao+1)
        if transicoes != None:
            return transicoes
    return None

def aceita(estados):
    if estados == None:
        return False
    for i in estados:
        for j in aceitacao:
            if i == j:
                return True
    return False

def imprimeCI(entrada, estado, posicao):
    print(entrada[0:posicao],end='')
    print("[q{}]".format(estado),end='')
    print(entrada[posicao:])

estados = [estado_inicial]

estados_finais = testa(entrada, estados, 0)

if aceita(estados_finais):
    print("ACEITA")
else:
    print("REJEITA")


