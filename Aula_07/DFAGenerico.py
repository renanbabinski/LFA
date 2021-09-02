# Código que roda um autômato determinístico dada sua tabela de transição e configurações iniciais

# Configuração instantânea do autômato
def imprimeCI(entrada, estado, posicao):
    print(entrada[0:posicao],end='')
    print("[q{}]".format(estado),end='')
    print(entrada[posicao:])

## Configuração do autômato
#########################
aceitacao = [1]

# estados = 0,1,2
# alfabeto = 0,1

transicao = [[0,1],
             [1,0]]

estado_inicial = 0
#########################

entrada = input("Digite a entrada\n")
estado = estado_inicial
posicao = 0

while posicao < len(entrada):
    imprimeCI(entrada, estado, posicao)

    elemento = entrada[posicao]
    elemento_int = int(elemento)

    estado = transicao[estado][elemento_int]
    
    posicao += 1

imprimeCI(entrada, estado, posicao)

aceita = False
for i in aceitacao:
    if estado == i:
        aceita = True


if aceita:
        print("ACEITA")
else:
    print("REJEITA")
