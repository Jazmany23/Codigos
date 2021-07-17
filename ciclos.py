# ciclos 
class Ciclos:
    def __init__(self,num1=0,num2=1):
        self.numero1=num1

    def usoWhile(self):
        # ciclo reetitivo que se ejecuta por verdadero y sale por falso

        car = input("Ingrese vocal: ")
        car = car.lower()
        while car not in('a','e','i','o','u'):
            car = input("Ingrese una  vocal: ").lower()
        print("""Felicidades el caracter ingresado : {} 
                es una vocal""".format(car))


# forma realizada hecha  clase
# class Ciclo:
#     def __init__(self, n1=0):
#         self.numero = n1

#     def usoWhilee(self):
#         caracter = input("Ingrese una vocal")
#         caracter = caracter.lower()
#         while caracter not in ("a", "e", "i", "o", "u"):
#             caracter = input("Ingrese una vocal").lower()
#         print("El caracter ingresado {} si es una vocal".format(caracter))
        
ciclo1 = Ciclos()
ciclo1.usoWhile()