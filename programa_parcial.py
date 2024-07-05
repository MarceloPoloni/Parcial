from funciones_parcial import *
import json

bikes = []
bandera_primer_ingreso =True
bandera_segundo_ingreso = False
seguir = "si"

while seguir == "si":
    match menu():
        case "1":
            limpiar_pantalla()
            try:
                nombre_archivo = input("ingrese el nombre del archivo a cargar : ")
                cargar_archivo_csv(f"{nombre_archivo}.csv",bikes)
                print("El archivo se cargo correctamente")
                bandera_primer_ingreso=False
            except:
                print("no se encontro ningun archivo con este nombre.")
                
        case "2":
            limpiar_pantalla()
            if bandera_primer_ingreso == False:
                mostrar_ciclistas_tabla(bikes)
        
        case "3":
            if bandera_primer_ingreso == False:
                mapear_lista(numeros_ramdom,bikes).append
                bandera_segundo_ingreso = False
                print("se cargaron los tiempos")
            else :
                print("primero debe cargar el archivo")
        
        case "4":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                print("tiempo/s ganador/es")
                mostrar_ciclistas_tabla(asignar_ganador(bikes))
                
            else:
                print("Primero debe cargar el archivo y asignarle los tiempos")
        
        case "5":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                crear_archivo_tipo(bikes)
                print("Archivo creado correctamente")
            else:
                print("Primero debe cargar el archivo y asignarle los tiempos")
                
            
        
        case "6":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                lista_tipos = ["BMX", "MTB", "PLAYERA"]
                for elementos in lista_tipos:
                    print(f"El promedio de las bicicletas {elementos} es {calcular_promedio(mapear_lista(lambda bike:bike["tiempo"],filtrar_lista(lambda tipe:tipe["tipo"] == elementos, bikes)))} minutos")
            else:
                print("Primero debe cargar el archivo y asignarle los tiempos")
                
            
        case "7":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                ordenar_por_dos_campos(bikes,"tipo","tiempo")
                mostrar_ciclistas_tabla(bikes)
            else:
                print("Primero debe cargar el archivo y asignarle los tiempos")
                
        case "8":
            limpiar_pantalla()
            if not bandera_primer_ingreso and not bandera_segundo_ingreso:
                ordenar_por_dos_campos(bikes, "tipo", "tiempo")
                with open(get_path_actual("bicis.json"), "w", encoding="utf-8") as archivo:
                    json.dump(bikes, archivo, indent=2)
                print("Archivo JSON creado con el listado ordenado")
            else:
                print("Primero debe cargar el archivo y asignarle los tiempos")
                
        case "9":
            limpiar_pantalla()
            print("Se cierra el programa, muchas gracias!")
            bandera_primer_ingreso = True
            bandera_segundo_ingreso= True
            break
        case _:
            print("Opción no válida. Intenta de nuevo.")
    pausar()
    seguir = input("¿Deseas continuar? (si/no): ").lower()
    if seguir == "no":
        print("muchas gracias , que tenga buen dia!") 
    else :
        print("ingrese opcion valida")
        