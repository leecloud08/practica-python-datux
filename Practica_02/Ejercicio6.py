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


#EJERCICIO 6
#Mostar el producto mas unidades vendidas

print("-"*50)
print("Listado de productos y unidades vendidas: ")
print("-"*50)

for i in ventas:
    print(f"Producto: {i['producto']}")
    print(f"Cantidad vendida: {i['cantidad']}")
    print("-"*50)


print("Producto más vendido: ")

producto_actual = {}
mayor_cantidad = 0

for i in ventas:
    if mayor_cantidad < i["cantidad"]:
        mayor_cantidad=i["cantidad"]
        producto_actual=i

print(f"Producto: {producto_actual['producto']}")
print(f"Cantidad: {producto_actual['cantidad']}")