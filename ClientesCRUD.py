def MainCrearUsuario():
    import json
    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    
    Clientes = mijson['Datos']['Clientes']

    NuevoCliente = {}

    NuevoCliente['Identificacion'] = int(input("Digite su identificación: "))
    NuevoCliente['Nombre'] = str(input("Digite su nombre: "))
    NuevoCliente['Apellido1'] = str(input("Digite un apellido: "))
    NuevoCliente['Apellido2'] = str(input("Digite el segundo apellido: "))
    NuevoCliente['Direccion'] = input("Digite su dirección: ")
    NuevoCliente['Telefono'] = int(input("Digite su telefono: "))
    NuevoCliente['Categoria'] = "Nuevo Cliente"
    NuevoCliente['Servicios'] = ""

    Clientes.append(NuevoCliente)

    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)

def MainEliminarUSuario():
    import json

    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    
    Clientes = mijson['Datos']['Clientes']

    x = input("Enter para mostrar lista de usuarios")
    print("----------------------")
    for i in Clientes:
        for key, value in i.items():
            print(f"{key} : {value}")
        print("----------------------")
    
    UserEliminar = int(input("Digite la tarjeta de identificación de la persona a eliminar: "))

    for Cliente in Clientes:
        if UserEliminar == Cliente['Identificacion']:
            Clientes.remove(Cliente)
    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)
    x = input("")


def MainActualizarUsuario():
    import json

    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    
    Clientes = mijson['Datos']['Clientes']
    Servicios = mijson['Datos']['Servicios']

    x = input("Enter para mostrar lista de usuarios")
    print("----------------------")
    for i in Clientes:
        for key, value in i.items():
            print(f"{key} : {value}")
        print("----------------------")
    
    UserActualizar = int(input("\nDigite la tarjeta de identificación de la persona a actualizar: "))

    for Cliente in Clientes:
        if UserActualizar == Cliente['Identificacion']:
            print("\nUsuario encontrado\n")
            print("Que desea actualizar del usuario?\n")
            print("1. Categoria\t2.Servicios")
            print("3. Usuario")

            OpcionAct = int(input("----->"))

            if OpcionAct == 1:
                print("Digite la categoría que desea actualizar")
                print("1. Nuevo Cliente\t2. Cliente Regular")
                print("3. Cliente Leal")
                OpcionCat = int(input("----->"))
                if OpcionCat == 1:
                    Cliente['Categoria'] = "Nuevo Cliente"
                if OpcionCat == 2:
                    Cliente['Categoria'] = "Cliente Regular"
                if OpcionCat == 3:
                    Cliente['Categoria'] = "Cliente Leal"
            elif OpcionAct == 2: 
                
                for Servicio in Servicios:
                    for key, value in Servicio.items():
                        print(f"{key} : {value}")
                    print("----------------------")
                print("Digite el Servicio que desea añadir al usuario: ")
                AñSer = int(input("------>"))

            elif OpcionAct == 3:

                Cliente['Identificacion'] = int(input("Digite la nueva identificación: "))
                Cliente['Nombre'] = str(input("Digite el nuevo nombre: "))
                Cliente['Apellido1'] = str(input("Digite el nuevo primer apellido: "))
                Cliente['Apellido2'] = str(input("Digite el nuevo segundo apellido: "))
                Cliente['Direccion'] = input("Digite su nueva dirección: ")
                Cliente['Telefono'] = int(input("Digite su nuevo telefono: "))
                Cliente['Categoria'] = Cliente['Categoria']
                Cliente['Servicios'] = Cliente['Servicios']
    
    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)
