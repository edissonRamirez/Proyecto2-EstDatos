from Aeropuerto import Aeropuerto
from Rutas import Rutas

aeropuerto1 = Aeropuerto("Aeropuerto Internacional JFK", "Nueva York, EE. UU.", "JFK")
aeropuerto2 = Aeropuerto("Aeropuerto de Heathrow", "Londres, Reino Unido", "LHR")

ruta1 = Rutas(aeropuerto1, aeropuerto2, "3oomts", "6 horas")

print(ruta1)