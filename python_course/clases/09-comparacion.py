class Coordenadas:
    def __init__(self, lat :float, lon :float) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, __value: object) -> bool:
        return self.lat == __value.lat and self.lon == __value.lon
    
    def __lt__(self, __value :object) -> bool:
        return self.lat + self.lon < __value.lon + __value.lat
    
    def __le__(self, __value :object) -> bool:
        return self.lat + self.lon <= __value.lon + __value.lat

coords = Coordenadas(45, 27)
coords2 = Coordenadas(46, 27)

print(coords != coords2)
print(coords <= coords2)
