print("clases version el constructor")
class perro:
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
        #funciones creadas por el usuario
    def muerde(self):
        print(f"chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro:{mensaje}")
    def chatperra(self,mensajep):
        print(f"chat perra:{mensajep}")
    def datos(self):
        print(f"color:{self.color} edad:{self.edad}")
#crear el objeto
chihuas=perro("negro",2)
#Llamadas a funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola canina")
chihuas.chatperra("hola bobi♥")
chihuas.chatperro("¿quieres ser mi gugguu? ♥")
chihuas.chatperra("grruuuuu♥")
