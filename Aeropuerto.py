class Aeropuerto:
    def __init__(self, nombre, ubicacion, codigo):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.codigo = codigo

    def __str__(self):
        return f"Aeropuerto: {self.nombre} ({self.codigo}), Ubicación: {self.ubicacion}"
        

    