largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
hasht = "#"

def retangulo(largura, altura, hasht):

    linha_c = hasht * largura
    if largura > 2:
        linha_v = hasht + (" " * (largura - 2)) + hasht
    else:
        linha_v = linha_c

    if altura >= 1:
        print(linha_c)
    for i in range(altura - 2):
        print(linha_v)
    if altura >= 2:
        print(linha_c)

retangulo(largura, altura, hasht)
