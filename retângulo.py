largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

linha = 0
coluna = 0

while linha < altura:
    while coluna > 1:
        print("#", end = " ")
        coluna = coluna + 1
    print()
    linha = linha + 1
    coluna = 0
        
        



