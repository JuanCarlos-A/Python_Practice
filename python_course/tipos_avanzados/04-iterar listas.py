mascotas = ["Pelusa", "Firulais", "Rex", "Milo", "Toby"]

for mascota in mascotas:
    print(mascota) # Pelusa Firulais Rex Milo Toby

for mascota in enumerate(mascotas):
    print(mascota) # (0, 'Pelusa') (1, 'Firulais') (2, 'Rex') (3, 'Milo') (4, 'Toby')

for indice, mascota in enumerate(mascotas):
    print(indice, mascota) # 0 Pelusa 1 Firulais 2 Rex 3 Milo 4 Toby

for mascota in enumerate(mascotas):
    print(mascota[0]) #  0 1 2 3 4
