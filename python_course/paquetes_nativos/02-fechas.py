# import time

# print(time.time())

from datetime import datetime

fecha = datetime(2024, 5, 2)

print(fecha)

ahora = datetime.now()

print(ahora)


fecha_str = datetime.strptime("2024-05-02", "%Y-%m-%d") 

print(fecha_str)

print(fecha.strftime("%Y/%m/%d"))

print(fecha < ahora)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute,
    fecha.second
)
