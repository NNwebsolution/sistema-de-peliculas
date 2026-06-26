peliculas = []

def mostrar_menu():
    print("===== MENÚ PRINCIPAL =====")
    print("1. Agregar Pelicula")
    print("2. Buscar Pelicula")
    print("3. Eliminar Pelicula")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar Peliculas")
    print("6. Salir")

def opcion():
    return int(input("Ingrese una opción: "))

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_duracion(duracion):
    return duracion > 0

def validar_calificacion(calificacion):
    return 0 <= calificacion <= 10


def agregar_pelicula(lista):
    titulo = input("Título: ")

    if not validar_titulo(titulo):
        print("Título invalido")
        return

    duracion = int(input("Duración: "))
    if not validar_duracion(duracion):
        print("Duración invalida")
        return

    calificacion = float(input("Calificación: "))
    if not validar_calificacion(calificacion):
        print("Calificación invalida")
        return

    pelicula = {
        "titulo": titulo,
        "duracion": duracion,
        "calificacion": calificacion,
        "disponible": False
    }

    lista.append(pelicula)
    print("Pelicula agregada.")


def buscar_pelicula(lista, titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i
    return -1


def actualizar_disponibilidad(lista):
    for pelicula in lista:
        if pelicula["calificacion"] >= 7:
            pelicula["disponible"] = True
        else:
            pelicula["disponible"] = False


def mostrar_peliculas(lista):
    actualizar_disponibilidad(lista)

    print("\n=== LISTA DE PeliculaS ===")

    for pelicula in lista:
        print("Título:", pelicula["titulo"])
        print("Duración:", pelicula["duracion"])
        print("Calificación:", pelicula["calificacion"])

        if pelicula["disponible"]:
            print("Estado: DISPONIBLE")
        else:
            print("Estado: NO RECOMENDADA")

        print("*" * 30)

while True:
    mostrar_menu()
    opcion = opcion()

    if opcion == 1:
        agregar_pelicula(peliculas)

    elif opcion == 2:
        titulo = input("Título a buscar: ")
        pos = buscar_pelicula(peliculas, titulo)

        if pos != -1:
            print("Pelicula encontrada:")
            print(peliculas[pos])
        else:
            print("Pelicula no encontrada.")

    elif opcion == 3:
        titulo = input("Titulo a eliminar: ")
        pos = buscar_pelicula(peliculas, titulo)

        if pos != -1:
            peliculas.pop(pos)
            print("Pelicula eliminada.")
        else:
            print(f"La Pelicula '{titulo}' no se encuentra registrada.")

    elif opcion == 4:
        actualizar_disponibilidad(peliculas)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        mostrar_peliculas(peliculas)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break

    else:
        print("Opción invalida.") ....