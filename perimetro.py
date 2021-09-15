class Triangulo:
    def __init__(self, a:int, b:int, c:int):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 0

        else:
            return self.a + self.b + self.c


    def tipo_lado(self)-> str:
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b != self.c or self.a != self.b == self.c or self.a == self.c != self.b:
                return "isóceles"

        else:
            return "escaleno"
        






    
        
