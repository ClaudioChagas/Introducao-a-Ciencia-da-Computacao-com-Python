def ordenada(list: list) -> bool:
    if not list:
        return False
    else:
        ordered_list = sorted(list)
        if ordered_list == list:
            return True 

        else:
            return False







def lista():
    lista =input("Digite sua lista: ")
    ordenada(list)
