class Condicion:
    contador=0 #variables de clases(opcional)
    #__init__ Metodo contructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que presenta la clase creada
    def __init__(self,num1=0,num2=1):
        self.numero1=num1# variables de instancia
        self.numero2=num2
        #numero = num1+num2
        self.numero3 = num1
        # variables de instancia 


    def usoIf(self):
        # if ... elif ... else ...: permiten condicionar de uno o varios bloques 
        # de sentencias al cimplimiento de una o varias condiciones.
        if self.numero1 == self.numero2:
            print("""numero1:{}, numero2:{}: 
            son iguales""".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
             print("""numero1:{}, numero3:{}: 
             son iguales""".format(self.numero1,self.numero3)) 
        else:
            print("no son iguales")
        

# usar clase 
            # cond1 = Condicion(8)
            # print(cond1.numero1)
            # print(cond1.numero2)

cond2 = Condicion(10,20)
cond2.usoIf() # llamada a un metodo de la clase   
print(cond2.numero1) # llamada a un atributo de la clase

