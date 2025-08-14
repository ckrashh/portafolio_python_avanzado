from agenda import Agenda

def val_campos(contacto):
    if len(contacto["nombre"]) == 0 or len(contacto["telefono"]) == 0 or len(contacto["correo"]) == 0:
        print("Por favor, ingrese todos los campos.")
        return True
    if not contacto["telefono"].isdigit() or len(contacto["telefono"]) != 11:
        print("Por favor, ingrese un telefono valido.")
        return True
    return False
def main():
    agenda = Agenda()
    while True:
        print("\n--- Menu Contactos ---")
        print("1. Agregar Contacto")
        print("2. Ver Contactos")
        print("3. Eliminar contacto")
        print("4. Salir")
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                contacto = {}
                while True:
                    contacto["nombre"] = input("Ingrese el nombre del contacto: ")
                    contacto["telefono"] = input("Ingrese el telefono del contacto (sin el + y de 11 digitos): ")
                    contacto["correo"] = input("Ingrese el correo del contacto: ")
                    if val_campos(contacto):
                        continue
                    break
                agenda.agregar_contacto(contacto)
            elif opcion == 2:
                agenda.mostrar_contactos()
            elif opcion == 3:
                while True:
                    nombre = input("Ingrese el nombre del contacto a eliminar: ")
                    if not nombre:
                        print("Por favor, ingrese el nombre del contacto a eliminar.")
                    else:
                        break
                agenda.eliminar_contacto(nombre)
            elif opcion == 4:
                print("Saliendo...")
                break
            elif opcion < 1 or opcion > 4:
                print("Por favor, ingrese una opcion valida.")
        except ValueError:
            print("Por favor, ingrese solo numeros.")
if __name__ == "__main__":
    main()