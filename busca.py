def busca_sequencial(seq, x):
    """(list, floaat) -> bool"""
    for i in range(len(seq)):
        if seq[i] == x:
            return True

        return False
