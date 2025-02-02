# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados

import os
class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []


    def asignar_horario(self, horario):
        """Asignando un horario a un conductor si no está ocupado en ese horario."""

        if horario in self.horarios:
            print(f"El conductor {self.nombre} ya tiene asignado el horario {horario}.")
            return False

        self.horarios.append(horario)
        print(f"Horario {horario} asignado a {self.nombre}.")
        return True


class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horario = None
        self.conductor = None


    def agregar_ruta(self, ruta):
        """Asignando una ruta al bus."""
        self.ruta = ruta
        print(f"Ruta {ruta} asignada al bus {self.id_bus}.")


    def registrar_horario(self, horario):
        """Registra el horario en el operará el bus."""
        self.horario = horario
        print(f"Horario {horario} registrado para el bus {self.id_bus}.")

    
    def asignar_conductor(self, conductor):
        """Asigna un conductor al bus si no se cruzan los horarios."""

        if self.horario is None:
            print(f"No puedes asignar un conductor si el bus {self.id_bus} no tiene horario.")
            return False

        if conductor.asignar_horario(self.horario):
            self.conductor = conductor
            print(f"Conductor {conductor.nombre} asignado al bus {self.id_bus}.")
            return True

        return False


class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    
    def agregar_bus(self, id_bus):
        """Crea un nuevo bus y lo agrega a la lista de buses."""
        bus = Bus(id_bus)
        self.buses.append(bus)
        print(f"Bus {id_bus} agregado con éxito.")
    

    def agregar_conductor(self, nombre):
        """Crea un nuevo conductor y lo agrega a la lista de conductores."""
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        print(f"Conductor {nombre} agregado con éxito.")

    
    def buscar_bus(self, id_bus):
        """Encuentra un bus por su ID."""
        for bus in self.buses:
            if bus.id_bus == id_bus:
                return bus

        print(f"No se encontró el bus {id_bus}. ")
        return None


    def buscar_conductor(self, nombre):
        """Encuentra un conductor por su nombre."""
        for conductor in self.conductores:
            if conductor.nombre == nombre:
                return conductor
        print(f"No se encontró el conductor {nombre}.")
        return None


    def menu(self):
        """Menú para gestionar los buses y conductores."""
        while True:
            print("\n=== MENÚ === ")
            print("1. Agregar bus")
            print("2. Agregar conductor")
            print("3. Asignar ruta a bus")
            print("4. Registrar horario a bus")
            print("5. Asignar conductor a bus")
            print("6. Agregar horario a conductor")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_bus = input("Ingrese el ID del bus: ")
                self.agregar_bus(id_bus)

            elif opcion == "2":
                nombre = input("Ingrese el nombre del conductor: ")
                self.agregar_conductor(nombre)

            elif opcion == "3":
                id_bus = input("Ingrese el ID del bus: ")
                bus = self.buscar_bus(id_bus)

                if bus:
                    ruta = input("Ingrese la ruta: ")
                    bus.agregar_ruta(ruta)

            elif opcion == "4":
                id_bus = input("Ingrese el ID sel bus: ")
                bus = self.buscar_bus(id_bus)

                if bus:
                    horario = input("Ingrese el horario (ejemplo: 8:00-12:00): ")
                    bus.registrar_horario(horario)

            elif opcion == "5":
                id_bus = input("Ingrese el ID del bus: ")
                bus = self.buscar_bus(id_bus)

                if bus:
                    nombre_conductor = input("Ingrese el nombre del conductor: ")
                    conductor = self.buscar_conductor(nombre_conductor)
                    if conductor:
                        bus.asignar_conductor(conductor)

            elif opcion == "6":
                nombre = input("Ingrese el nombre del conductor: ")
                conductor = self.buscar_conductor(nombre)

                if conductor:
                    horario = input("Ingrese el horario a signar (ejemplo: 8:00-12:00): ")
                    conductor.asignar_horario(horario)
                
            elif opcion == "7":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida. Intente nuevamente.")

#Ejecutar el programa
admin = Admin()
admin.menu()