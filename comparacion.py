
def __init__(self, latitud, longitud):
    self.latitud = self.validar_latitud(latitud)
    self.longitud = self.validar_longitud(longitud)
def validar_latitud(self, latitud):
    if not isinstance(latitud, float) or latitud < -90 or latitud > 90:
        raise ValueError("La latitud debe ser un número entre -90 y 90.")
    return latitud
def validar_longitud(self, longitud):
    if not isinstance(longitud, float) or longitud < -180 or longitud > 180:
        raise ValueError("La longitud debe ser un número entre -180 y 180.")
    return longitud
coords = (10.0, 20.0)
coords2 = (10.0, 20.0)


print(coords, coords2)