# num=20
# if type(num) == int:
#     print("respuenta" ,num*2)
# else:
#     print("el dato no va a ser numertico")

# def mensaje(men):
#     print(men)

# mensaje("Hola Adonis")
# mensaje("Saludame a tu hermana ")

# class Carlita:
#     def useVariables(self):
#         edad, _peso = 50, 80.90
#         print(edad,_peso)


# ejer1 = Carlita()
# ejer1.useVariables()



class Sintaxis:
    instancia=0
    

    def __init__(self, dato="Inicializacion"):
        self.frase=dato
        #Sintaxis.instancia = Sintaxis.instancia+1


    def useVariables(self):
        edad,_peso = 20, 92.90
        nombres = "Jazmany Correa"
        Tiposexo = "M"
        civil = True


        usuario=()
        usuario=("Jazrro23", 124525,"lamechec@gmail.com",True)
        # usuario[3]="Milagro"

        materias=[]
        materias=["PHP","POO","Proweb"]
        materias[1]="Python"
        materias.append("Go")
        # diccionarios = {} colecciones de objetos clave:valor tipo json
        alumno={}
        alumno={'nombre': 'Jazmany', 'edad': 20, 'fac': 'faci'}
        #alumno["carrera"]= "Ingenieria en Software"
        
# presentacion con format 
        # print("""Mi nombre es {}, tengo {}
        #         años""".format(nombres, edad))



        # print(usuario,materias,alumno)
        # print(usuario,usuario[0],usuario[0:2],usuario[-1])
        # print(materias,materias[2:],materias[:3],materias[::],materias[-2:] )
        print(alumno,alumno['nombre']) 

        

ejer1= Sintaxis()
ejer1.useVariables()

        

