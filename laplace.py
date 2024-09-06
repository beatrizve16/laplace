#PARTE 1
def matriz():
  #solicita ao usuario o tamanho da matriz e declara a variavel N pra ser esse tamanho
    n = int(input("Digite o tamanho da matriz (n x n): "))

    #inicia uma lista vazia que vai guardar essa matriz que sera digitada
    matriz = []

    #comeca um loop do tamanho que o usuario digitou pra cada linha
    for i in range(n):
        linha = [] # cria uma lista ´pra guardar os valores de cada linha

        print(f"Digite os numeros da linha {i}:")

        #novo loop so que para as colunas
        for j in range(n):

            #recebe cada numero da matriz
            num = input(f"numero [{i},{j}]: ")

            #coloca o numero na lista da linha que esta sendo percorrida
            linha.append(num)
#depois de ver todas as linhas adiciona a linha na matriz
        matriz.append(linha)
#retorna a matriz completa
    return matriz


#PARTE 2
# Função para criar uma matriz menor removendo a linha i e a coluna j
def matrizMenor():

    # Cria uma lista vazia para guardar a matriz menor
    matrizMenor = []

# falta continuar nao sei ainda o que fazer kkkk 



#PARTE 3 
# Função para calcular o determinante 
def determinante(matriz):

    # Obtém o número de linhas/colunas da matriz
    n = len(matriz)

    # matriz 1x1
    if n == 1:
        # Retorna o único numero da matriz 1x1 como o determinante
        return matriz[0][0]
    
    # matriz 2x2
    if n == 2:
        # Calcula o determinante de uma matriz 2x2:
        # det = a11 * a22 - a12 * a21
        return (matriz[0][0] * matriz[1][1])- (matriz[0][1] * matriz[1][0])
#o resto n sei 


#PARTE 4- o final implementando tudo
matriz = matriz()
print("O determinante da matriz é:", determinante(matriz))

