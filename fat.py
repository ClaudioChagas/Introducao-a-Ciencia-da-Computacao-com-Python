fat = int(input("Digite um número para torná-lo fatorial: "))
while fat >= 0:
    fatorial = 1
    while fat > 1:
       fatorial = fatorial * fat
       fat = fat - 1
    print(fatorial)
    fat = int(input("Digite um número negativo pata terminar: "))
    
        
