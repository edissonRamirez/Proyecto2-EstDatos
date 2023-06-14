import networkx as nx

class GrafoAeropuertos:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_aeropuerto(self, nombre, ubicacion, codigo):
        self.grafo.add_node(codigo, nombre=nombre, ubicacion=ubicacion)

    def editar_aeropuerto(self, codigo, nombre=None, ubicacion=None):
        if nombre:
            self.grafo.nodes[codigo]['nombre'] = nombre
        if ubicacion:
            self.grafo.nodes[codigo]['ubicacion'] = ubicacion

    def agregar_ruta(self, origen, destino, distancia, tiempo_vuelo):
        self.grafo.add_edge(origen, destino, distancia=distancia, tiempo_vuelo=tiempo_vuelo)

    def editar_ruta(self, origen, destino, distancia=None, tiempo_vuelo=None):
        if distancia:
            self.grafo[origen][destino]['distancia'] = distancia
        if tiempo_vuelo:
            self.grafo[origen][destino]['tiempo_vuelo'] = tiempo_vuelo


# Crear una instancia del grafo de aeropuertos
grafo_aeropuertos = GrafoAeropuertos()

# Agregar aeropuertos
grafo_aeropuertos.agregar_aeropuerto("Aeropuerto Internacional JFK", "Nueva York, EE. UU.", "JFK")
grafo_aeropuertos.agregar_aeropuerto("Aeropuerto Internacional de Los Ángeles", "Los Ángeles, EE. UU.", "LAX")

# Agregar una ruta
grafo_aeropuertos.agregar_ruta("JFK", "LAX", 500, 2.5)

# Editar un aeropuerto
grafo_aeropuertos.editar_aeropuerto("JFK", nombre="Aeropuerto JFK")

# Editar una ruta
grafo_aeropuertos.editar_ruta("JFK", "LAX", tiempo_vuelo=3.0)
