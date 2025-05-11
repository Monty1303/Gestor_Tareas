def agregar_tarea(lista,tarea):
    lista.append(tarea)
    return lista
# Función Listar Tareas

def listar_tareas(lista):
    if not lista:
        print("la lista está vacia")
    for id,tarea in enumerate(lista,start=1):
            print(f"{id}-{tarea}")