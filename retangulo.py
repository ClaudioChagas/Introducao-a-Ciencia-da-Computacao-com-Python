largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
hasht = "#"

def retangulo(hasht, largura, altura):

    linha = hasht * largura
    for i in range(altura):
        print(linha)
    
retangulo(hasht, largura, altura)
