from datetime import timedelta, datetime

fecha1 = datetime(2023, 1, 1, 12, 0, 0) +timedelta(days=4, hours=12)
fecha2 = datetime(2023, 5, 5, 12, 0, 0)

delta = fecha2 - fecha1
print(delta)
print("dias:", delta.days)
print("segundos:", delta.seconds)
print("microsegundos:", delta.microseconds)
print("total segundos:", delta.total_seconds())
