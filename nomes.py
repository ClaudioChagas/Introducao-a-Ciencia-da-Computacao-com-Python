def menor_nome(nomes):

    nomeCurto = nomes[0]
    comprimentoDoNomeCurto = len(nomes[0])

    for nome in nomes:
       nome = nome.strip()
       if len(nome) < comprimentoDoNomeCurto:
           comprimentoDoNomeCurto = len(nome)
           nomeCurto = nome

    return nomeCurto.capitalize()
