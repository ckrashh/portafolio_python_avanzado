from contacto import Contacto
class Agenda():
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, contacto):
        if self.existe(self.contactos, contacto["nombre"]):
            print("El contacto ya existe.")
            return
        contacto = Contacto(contacto["nombre"], contacto["telefono"], contacto["correo"])
        print("\nContacto agregado exitosamente.")
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return
        for contacto in self.contactos:
            print(contacto)

    def eliminar_contacto(self, nombre):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return
        for contacto in self.contactos:
            if contacto._nombre == nombre:
                self.contactos.remove(contacto)
                print("Contacto eliminado exitosamente.")
                return
        print("\nEl contacto no existe")
    
    @staticmethod
    def existe(contactos, nombre):
        for contacto in contactos:
            if contacto._nombre == nombre:
                return True
        return False