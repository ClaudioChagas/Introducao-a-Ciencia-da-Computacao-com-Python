def soma_matrizes(m1, m2):
    matriz_soma = []
    quant_linhas = len(m1) 
    quant_colunas = len(m1[0]) 
  
    for i in range(quant_linhas):
        matriz_soma.append([])
        for j in range(quant_colunas):
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma
       
   
m1 = input("digite a matriz 1: ")
m2 = input("digite a matriz 2: ")
