
import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
database = client["unl"]
collection = database["items"]


def crear_registro():
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    datos = {"nombre": nombre, "edad": edad}
    collection.insert_one(datos)
    print("Registro creado con éxito.")


def leer_registros():
    registros = collection.find()
    print("Registros existentes:")
    for registro in registros:
        print(f"Nombre: {registro['nombre']}, Edad: {registro['edad']}")


def actualizar_registro():
    nombre = input("Ingrese el nombre del registro a actualizar: ")
    query = {"nombre": nombre}
    nuevo_nombre = input("Ingrese el nuevo nombre: ")
    nueva_edad = int(input("Ingrese la nueva edad: "))
    nuevos_datos = {"$set": {"nombre": nuevo_nombre, "edad": nueva_edad}}
    collection.update_one(query, nuevos_datos)
    print("Registro actualizado con éxito.")


def eliminar_registro():
    nombre = input("Ingrese el nombre del registro a eliminar: ")
    query = {"nombre": nombre}
    collection.delete_one(query)
    print("Registro eliminado con éxito.")


while True:
    print("\n--- MENÚ ---")
    print("1. Crear registro")
    print("2. Leer registros")
    print("3. Actualizar registro")
    print("4. Eliminar registro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_registro()
    elif opcion == "2":
        leer_registros()
    elif opcion == "3":
        actualizar_registro()
    elif opcion == "4":
        eliminar_registro()
    elif opcion == "5":
        break
    else:
        print("Opción inválida. Intente nuevamente.")


client.close()