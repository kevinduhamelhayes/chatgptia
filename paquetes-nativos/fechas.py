# import time
# print(time.time())

from datetime import datetime

fecha = datetime(2023, 1, 1, 12, 0, 0)
print(fecha)

ahora = datetime.now()
print(ahora)

fechaString = datetime.strptime("2023-01-01 12:00:00", "%Y-%m-%d %H:%M:%S")
print(fechaString)