def agregar_tarea(lista,tarea):
    lista.append(tarea)
    return lista
# Función Listar Tareas

def listar_tareas(lista):
    if not lista:
        print("la lista está vacia")
    for id,tarea in enumerate(lista,start=1):
            print(f"{id}-{tarea}")


# Función Eliminar Tareas

def eliminar_tareas(lista,indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    else:
        print("Indice fuera del rango")

    print()
