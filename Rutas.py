class Rutas:
    def __init__(self, inicio, final, distancia, tVuelo):
        self.punto_partida = inicio
        self.punto_llegada = final
        self.distancia_vuelo = distancia
        self.tiempo_vuelo = tVuelo

    def __str__(self):
        return f"Vuelo desde ({self.punto_partida}) hasta ({self.punto_llegada}), Duración de vuelo: {self.tiempo_vuelo}, Distancia: {self.distancia_vuelo}"