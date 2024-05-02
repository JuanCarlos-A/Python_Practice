from datetime import datetime, timedelta

fecha1 = datetime(2024, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2024, 2, 1)

delta = fecha2 - fecha1


print(delta)

print(f' Dias : {delta.days}')
print(f' Segundos : {delta.seconds}')
print(f' MicroSegundos : {delta.microseconds}')
print(f' Total de Segundos : {delta.total_seconds()}')
