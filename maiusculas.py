def maiusculas(frase):
    maiusculas = []
    
    for i in range(len(frase)):
        caractere = frase[i]
        dec = ord(caractere)

        if dec > 64 and dec < 91:
            
            maiusculas.append(caractere)

    return "".join(maiusculas)


def teste():
    assert maiusculas("Programamos em python 2?") == "P"
