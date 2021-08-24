N = int(input("Digite um número: "))

soma=1
while (N > 0):
        resto= N % 2
        N= (N - resto)/2
        soma= soma + resto

print("A soma dos números é: ", N)
