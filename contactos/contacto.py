class Contacto:
    def __init__(self, nombre, telefono, correo):
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo

    def __str__(self):
        return f"Nombre: {self._nombre}, Telefono: {self._telefono}, Correo: {self._correo}"
    