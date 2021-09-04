#import random

def geraMatriz(t):
    global vetor1
    global matriz

    # prepara o vetor para formar a matriz
    for n in range(t):
        vetor1.append(list())

    multiplicador = t
    for n in range(multiplicador):
        matriz.append(list(vetor1))

    # imprime a matriz
    for linha in range(t):
        for coluna in range(t):
            #if coluna % 2 == 0 and linha % 2 == 0:                ----------So um teste para ver se estava funfando :D
                #matriz[linha][coluna] = random.randint(1, 10)
            print(matriz[linha][coluna], end='')
        print()


if __name__ == '__main__':
    vetor1 = []
    matriz = []

    dimensoes = int(input('Quantas dimensões? ')) # tamanho da matriz
    geraMatriz(dimensoes)
