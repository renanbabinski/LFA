#Exercício: Descobrir o que faz o autômato abaixo

# Configuração do Autômato
#############################

aceitacao = {0}
estado_inicial = [0]

#estados 0,1,2,...
#alfabeto 0,1,2

transicao = [[[1], [],  []],
             [[],  [2], [2]],
             [[],  [],  []]]

transicao_vazia = [[], [0], [0]]

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
    print(entrada[0:posicao]+"{",end='')

    for i in range(0, len(estados)):
        print("q"+str(estados[i]),end='')
        if(i < len(estados)-1):
            print(";",end='')

    print("}"+entrada[posicao:])

def uniao(estados, novos_estados):
    uniao = set()
    for i in estados:
        uniao.add(i)
    for i in novos_estados:
        uniao.add(i)

    ret = list(uniao)
    return ret

def eclose(estados):
    eclose_ = estados

    for i in estados:
        eclose_aux = transicao_vazia[int(i)]
        eclose_aux_2 = eclose(eclose_aux)
        eclose_ = uniao(eclose_, eclose_aux)
        eclose_ = uniao(eclose_, eclose_aux_2)

    return eclose_

########################################

posicao = 0

estados = eclose(estado_inicial)

while(posicao < len(entrada)):
    imprimeCI(entrada, estados, posicao)
    elemento = int(entrada[posicao])

    novos_estados = []

    for i in estados:
        destino_transicao = transicao[i][elemento]
        novos_estados = uniao(novos_estados, destino_transicao)
        novos_estados = eclose(novos_estados)
    
    estados = novos_estados
    if len(estados) == 0:
        break

    posicao += 1

imprimeCI(entrada, estados, posicao)

    

if aceita(estados):
    print("ACEITA")
else:
    print("REJEITA")


