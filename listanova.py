lista = input("Lista: ")

def remove_repetidos (remove_repetidos):
    l = []
    for i in remove_repetidos :
        if i not in l:
            l.append(i)
    l.sort()
    return l

remove_repetidos = [1, 2, 3]

l = remove_repetidos(remove_repetidos)
print (l)
