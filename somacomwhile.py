print("Digite um valor a ser somado terminada por 0: ")

soma= 0
valor= 1

while valor != 0:
	valor= int(input("Digite um valor a ser somado: "))
	soma= soma + valor 
	
print("O soma dos valores digitados é: ", soma)