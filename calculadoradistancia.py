X = int(input("Digite a primeira coordenada X: "))
Y=  int(input("Digite a segunda coordenada Y: "))

x= int(input("Digite a primeira coordenada x: "))
y= int(input("Digite a segunda coordenada y: "))

import math 

distancia = ( (X - x) ** 2) + ( (Y - y)  ** 2)
math.sqrt(distancia)


if distancia >= 10:
    print("longe")
if distancia < 10: 
    print("perto")

