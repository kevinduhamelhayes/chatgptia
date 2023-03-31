for j in range(1, 100):
    print(j)
    for i in range(1, 100):
        print(i)
        if i == 99:
            break
    else:
        print("No se encontro el numero")
    print("Fin del for interno")