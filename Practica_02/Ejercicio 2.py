import os
os.system("cls")

# PRACTICA NRO 2
#  DEFINA EL SIGUIENTE DICCIONARIO "VENTAS "
ventas=[
    {
        "fecha":"12-01-2023",
        "producto":"Producto_A",
        "cantidad":50,
        "precio":45.00,
        "promocion":True
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_AX",
        "cantidad":160,
        "precio":12.00,
        "promocion":False
    },
    {
        "fecha":"10-01-2023",
        "producto":"Producto_D",
        "cantidad":20,
        "precio":15.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_C",
        "cantidad":10,
        "precio":140.00,
        "promocion":False
    },
    {
        "fecha":"11-01-2023",
        "producto":"Producto_D",
        "cantidad":1200,
        "precio":1.00,
        "promocion":True
    }
]


#EJERCICIO 2
#Mostrar el listado de ventas
print("-"*50)
print("Listado de ventas: ")
print("-"*50)
for i in ventas:
    print(f"Fecha: {i['fecha']}")
    print(f"Producto: {i['producto']}")
    print(f"Cantidad: {i['cantidad']}")
    print(f"Precio: {i['precio']}")
    print(f"Promoción: {"Sí" if i['promocion'] else "No"}")

    print("-"*50)