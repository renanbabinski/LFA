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

def aceita(estados):
    if estados == None:
        return False
    for i in estados:
        for j in aceitacao:
            if i == j:
                return True
    return False

def imprimeCI(entrada, estados, posicao):
    print(entrada[0:posicao],end='')
    print("[q{}]".format(estado),end='')
    print(entrada[posicao:])

def uniao(estados, novos_estados):
    uniao = set()
    for i in estados:
        uniao.add(i)
    for i in novos_estados:
        uniao.add(i)

    ret = list(uniao)
    return ret

########################################

posicao = 0

estados = [estado_inicial]

while(posicao < len(entrada)):
    imprimeCI(entrada, estados, posicao)
    elemento = int(entrada[posicao])

    novos_estados = []

    for i in estados:
        destino_transicao = transicao[i][elemento]
        novos_estados = uniao(novos_estados, destino_transicao)
    
    estados = novos_estados
    if len(estados) == 0:
        break

    posicao += 1

    imprimeCI(entrada, estados, posicao)

    

if aceita(estados_finais):
    print("ACEITA")
else:
    print("REJEITA")


