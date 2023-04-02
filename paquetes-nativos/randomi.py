import random
import string
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
lista2 = random.sample(lista, 5)
print(random.randint(1, 10),
      random.random(),
      random.choice(lista),
    lista)


chars = string.ascii_letters + string.digits
selected_chars = random.choices(chars, k=10)
password = "".join(selected_chars)
print(password)