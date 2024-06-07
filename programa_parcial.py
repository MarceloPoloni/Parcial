from funciones_parcial import *

bikes = []
# # 1,2) bicicletas.csv
# csv_filename = input("ingrese el nombre del archivo a cargar : ")
# if(isinstance(csv_filename, str)):
#     bikes = read_csv(csv_filename)
#     # print(bikes)

# print()
# print("--------------------------------------------------------")
    
# # 3) 
# print (asignar_tiempos(bikes))

# print()
# print("--------------------------------------------------------")

# # 4)
# print (obtener_ganador(bikes))

# #6)
# print (promedio_por_tipo(bikes))


bandera_primer_ingreso =False
bandera_segundo_ingreso = False
seguir = "si"
while seguir == "si":
    match menu():
        case "1":
            csv_filename = input("ingrese el nombre del archivo a cargar : ")
            if(isinstance(csv_filename, str)):
                bikes = read_csv(csv_filename)
                print(bikes)
                bandera_primer_ingreso=True
        case "2":
            print (asignar_tiempos(bikes))
            bandera_segundo_ingreso = True
        case "3":
            print (obtener_ganador(bikes))
        case "4":
            print (promedio_por_tipo(bikes))
        case "5":
            print (filtrar_tipo(bikes, "playera"))
            
        case "6":
            bandera_primer_ingreso =False
            bandera_segundo_ingreso = False
            break
        
    pausar()