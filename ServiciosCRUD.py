def MainServiciosAñadir():
    import json
    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    
    Servicio = mijson['Datos']['Servicios']
    
    NuevoServicio = {}

    NuevoServicio['Servicio'] = str(input("Digite el nombre del servicio: ")).capitalize()
    NuevoServicio['Precio'] = float(input("Digite el precio del servicio: "))
    NuevoServicio['Caracteristicas'] = str(input("Digite las caracteristicas que tiene el servicio: "))

    Servicio.append(NuevoServicio)

    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)
    

def MainServiciosEliminar():
    import json

    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)

    Servicios = mijson['Datos']['Servicios']

    x = input("Enter para mostrar lista de Servicios")
    print("----------------------")
    for Servicio in Servicios:
        for key, value in Servicio.items():
            print(f"{key} : {value}")
        print("----------------------")
    
    ServicioEli = str(input("Digite el nombre del servicio para eliminarlo: ")).capitalize()

    for Servicio in Servicios:
        if ServicioEli == Servicio['Servicio']:
            Servicios.remove(Servicio)

    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)
    

def MainServiciosActualizar():
    import json
    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    Servicios = mijson['Datos']['Servicios']
    
    x = input("Enter para mostrar lista de Servicios")
    print("----------------------")
    for Servicio in Servicios:
        for key, value in Servicio.items():
            print(f"{key} : {value}")
        print("----------------------")
    ServicioAct = str(input("Digite el nombre del servicio para Actualizarlo: ")).capitalize()

    for Servicio in Servicios:
        if ServicioAct == Servicio['Servicio']:
            print("\nServicio Encontrado\n")
            
            Servicio['Servicio'] = str(input("Digite el nuevo nombre del servicio: ")).capitalize()
            Servicio['Precio'] = float(input("Digite el nuevo precio del servicio: "))
            Servicio['Caracteristicas'] = str(input("Digite las nuevas caracteristicas: "))
            
    with open('Datos.json','w',encoding="utf8") as infile:
        json.dump(mijson,infile,indent=2)


def MainServiciosListar():
    import json
    with open('Datos.json','r',encoding="utf8") as outfile:
        mijson = json.load(outfile)
    Servicios = mijson['Datos']['Servicios']

    x = input("Enter para mostrar lista de Servicios")
    print("----------------------")
    for Servicio in Servicios:
        for key, value in Servicio.items():
            print(f"{key} : {value}")
        print("----------------------")
    x = input("Presione enter para continuar")