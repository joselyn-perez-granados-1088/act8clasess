class Informacion:
    def mi_lista(self):
        lista_nombreperros=["kilo","kenda","kimbo"]
        for x in lista_nombreperros:
            print(x)

    def mi_tupla(self):
        tupla_edadperros=("15","1","5")
        for x in tupla_edadperros:
            print(x)

    def mi_diccionario(self):
        diccionario_razaperros={
            "perro 1: ":"husky",

            "perro 2: ": "pitbull",

            "perro 3: ": "cane"
                                }
        for x,y in diccionario_razaperros.items():
            print(x,y)

    def mi_conjunto(self):
        conjunto_colorperros={"cafe","merle","panda"}
        for x in conjunto_colorperros:
            print(x)
        # creando el objeto
datos=Informacion()
print("listado de nombres de perros")
datos.mi_lista()

print("tupla de edad de perros")
datos.mi_tupla()

print("diccionario de raza de perros")
datos.mi_diccionario()

print("conjunto de color de perros")
datos.mi_conjunto()