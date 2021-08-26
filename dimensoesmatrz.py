def dimensoes(matriz):
    colunas = 0
    linhas = 0
    qtd_colunas = 0
    a = ''
    for i in range(len(matriz)):
        linhas = linhas + 1 
        colunas = matriz[i] 
    for w in colunas: 
        qtd_colunas = qtd_colunas + 1
    a = print('{}X{}'.format(linhas, qtd_colunas))

    return a


matriz = input("Digite a raiz: ")

   

