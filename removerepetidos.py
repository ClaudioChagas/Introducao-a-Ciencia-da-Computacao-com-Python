def remove_repetidos(lista):
	for numero in lista:
		if numero not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numero)
	for numeroCorrente in lista:
		if numeroCorrente not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numeroCorrente)

	while len(listaDeNumerosUnicos) > 0:
		
		numeroMinimo = min(listaDeNumerosUnicos)
		listaOrdenada.append(numeroMinimo)

		index = listaDeNumerosUnicos.index(numeroMinimo)
		del listaDeNumerosUnicos[index]

	return sorted(listaDeNumerosUnicos)
	return listaOrdenada

remove_repetidos = int(input("Digite uma lista: "))
