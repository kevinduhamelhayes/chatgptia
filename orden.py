# lista_de_numeros_desordenada = [221, 12, 30, 4, 51, 6, 7, 8, 9, 10]
# lista_de_numeros_desordenada.sort(reverse=True)
# numeros2=sorted(lista_de_numeros_desordenada, reverse=True)
usuarios = [
["juan", 30],
["jacinto",25],
["miguel",27]]

# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
#traer un elemento en una lista y transformarla en otra lista
nombres = [usuario[0] for usuario in usuarios]
print(nombres)
#filtrar y transformar
nombres2 = [usuario[0] for usuario in usuarios if usuario[1] > 26]
print(nombres2)


monjas = [
["juana", 30],
["jacinta",25],
["miguela",27]]
nombesdemonjas = list(map(lambda usuario: usuario[0], monjas))
print(nombesdemonjas)
monajasmayores = list(filter(lambda usuario: usuario[1] > 26, monjas))
print(monajasmayores)