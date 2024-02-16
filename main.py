import os
import ClientesCRUD
import ServiciosCRUD
def limpiarterminal():
    os.system("cls")
    os.system("clear")


while True:
    limpiarterminal()
    print("********************************")
    print("*   BIENVENIDO A MI MOVISTAR   *")
    print("********************************")
    print("\nA que modulo desea ingresar?")
    print("1. Usuarios\t2. Servicios")
    print("3. Reportes\t4. Clientes Leales")
    print("5. Salir")
    opcion = int(input("Ingrese una opcion: "))
    while True:
        if opcion == 1:
            limpiarterminal()
            print("********************************")
            print("*        MODULO USUARIOS       *")
            print("********************************")
            print("Que desea hacer en el modulo usuarios?\n")
            print("1. Crear usuario\t 2. Eliminar usuario")
            print("\n3. Actualizar usuario\t 4. Regresar al modulo anterior")
            print("\n")
            OpcionUser = int(input("Ingrese una opcion: "))
            if OpcionUser == 1:
                limpiarterminal()
                print(ClientesCRUD.MainCrearUsuario())
            elif OpcionUser == 2:
                limpiarterminal()
                print(ClientesCRUD.MainEliminarUSuario())
                x = input("")
            elif OpcionUser == 3:
                print("Actualizar usuario")
                print(ClientesCRUD.MainActualizarUsuario())
            elif OpcionUser == 4:
                break
            else:
                print("Opcion no valida")
                x = input("")
        elif opcion == 2:
            limpiarterminal()
            print("********************************")
            print("*        MODULO SERVICIOS      *")
            print("********************************")
            print("Que desea hacer en el modulo de servicios?\n")
            print("1. Crear servicio\t2. Eliminar servicio")
            print("\n3. Actualizar Servicio \t4. Mostrar lista de servicios")
            print("\n5. Regresar al modulo anterior")
            OpcionServicios = int(input("Ingrese una opcion: "))
            
            if OpcionServicios == 1:
                limpiarterminal()
                print(ServiciosCRUD.MainServiciosAñadir())
                
            elif OpcionServicios == 2:
                limpiarterminal()
                print(ServiciosCRUD.MainServiciosEliminar())
    
            elif OpcionServicios == 3:
                limpiarterminal()
                print(ServiciosCRUD.MainServiciosActualizar())
                
            elif OpcionServicios == 4:
                print(ServiciosCRUD.MainServiciosListar())
            elif OpcionServicios == 5:
                break
            else:
                print("Opcion no valida")
                x = input("")
        elif opcion == 3:
            limpiarterminal()
            print("********************************")
            print("*        MODULO REPORTES       *")
            print("********************************")
            print("Que desea hacer en el modulo de reportes?\n")
            print("1. Cantidad de productos ofrecidos por la empresa")
            print("2. Servicios populares")
            print("3. Informes sobre usuarios que han adquirido cada servicio y con ello la cantidad de este mismo.")
            print("4. Regresar al modulo anterior")
            
            opcionReportes = int(input("Ingrese una opción: "))

            if opcionReportes == 1:
                limpiarterminal()
                print("Cantidad de productos ofrecidos por la empresa")
                print(ServiciosCRUD.MainServiciosListar())

            elif opcionReportes == 2:
                print("Servicios populares ")
                x = input("")
            elif opcionReportes == 3:
                print("Informes sobre usuarios que han adquirido cada servicio y con ello la cantidad de este mismo.")
                x = input("")
            elif opcionReportes == 4:
                break
            else:
                print("Opcion no valida")
                x = input("")

        elif opcion == 4:
            limpiarterminal()
            print("********************************")
            print("*    MODULO CLIENTES LEALES    *")
            print("********************************")
            print("Que desea hacer en el modulo de clientes leales?\n")
            print("1. Listar clientes leales\t 2. Asignar bonificaciones")
            print("3. Regresar al modulo anterior")
            OpcionLeales = int(input("Ingrese una opción: "))

            if OpcionLeales == 1:
                print("Listar clientes leales")
                x = input("")
            elif OpcionLeales == 2:
                print("ASignar bonificaciones")
                x = input("")
            elif OpcionLeales == 3:
                break
            else:
                print("Opcion no valida")
                x = input("")
        elif opcion == 5:
            print(" Hasta luego!")
            x = input("")
            break
        else:
            print("\nOpcion no valida, digite un valor dentro del rango")
            x = input("")