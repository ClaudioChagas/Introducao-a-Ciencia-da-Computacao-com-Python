def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

    lista = remove_repetidos(lista)
    print (lista)

###############

lista = input("digite uma lista: ")
