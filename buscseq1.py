def busca(list: list, element):
    for i, el in enumerate(list):
        if element == el:
            return i
    return False
