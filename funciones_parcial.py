from os import system
import csv
import random
import os




def get_path_actual (filename):
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, filename)
# ----------------------------------------------------------------

def read_csv (filename):
    bikes = []
    with open (get_path_actual(filename), "r", encoding="UTF-8") as archivo_csv:
        contenido = csv.reader(archivo_csv, delimiter=',')
        next(contenido)
        for fila in contenido:
            bikes.append(fila)
    
    return bikes
# ----------------------------------------------------------------
def asignar_tiempos (bikes) :
    for bike in bikes :
        bike[3] = random.randint(50,120)
    return bikes
# ----------------------------------------------------------------


def calcular_menor(lista:list)->int:

    if len(lista) == 0:
        raise ValueError("No esta definido el menor de una lista vacía")
    flag_primer_elemento = True
    for elemento in lista:
        if flag_primer_elemento == True or menor > elemento:
            flag_primer_elemento = False
            menor = elemento

    return menor

def obtener_ganador(bikes) :
    minimo = calcular_menor(bikes) 
    ganadores = [bike for bike in bikes if bike[3] == minimo[3]]
    print (ganadores)

    if not ganadores:
        return "No hay ganadores."

    if(len(ganadores) == 1) :
        return (f"El ganador es {ganadores[0][1]} con tiempo de {ganadores[0][3]}")
    else :
        return (f"Los ganadores son: {ganadores}")

    
    
    # ganador = calcular_menor(bikes) 
    # ganadores = [bike for bike in bikes if bike[3] == ganador[3]]
    # if(len(ganador) == 1) :
    #     return (f"El ganador es {ganador[0][1]} con tiempo de {ganador[0][1]}")
    # elif(len(ganadores) > 1) :
    #     return (f"Los ganadores son : {ganadores}")
    # else :
    #     return "error"
    
    
def obtener_tipos_bicicletas_sin_repetir (bikes:list) -> list:
    tipos = [] 
    for bike in bikes:
        if not bike[2] in tipos:
            tipos.append(bike[2])
    
    print(tipos)
    return tipos

def promedio_por_tipo(bikes) :
    bikes_con_tiempo = asignar_tiempos(bikes)
    promedios = []
    for tipo in obtener_tipos_bicicletas_sin_repetir(bikes_con_tiempo) :
        total = 0
        for bike in bikes :
            if(bike[2] == tipo) :
                total += int(bike[3])
        promedios.append((tipo, total / len(obtener_tipos_bicicletas_sin_repetir(bikes))))
    
    
    return promedios
    

def filtrar_tipo(bikes, tipo) :
    lista_filtrada_tipo = [bike for bike in bikes if bike[2] == tipo]
    with open(f"{tipo}.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        for bike in lista_filtrada_tipo :
            writer.writerow(bike)

def limpiar_pantalla ():
    return system ("cls")
def pausar ():
    return system("pause")

def menu():
    limpiar_pantalla()
    print("   MENU DE OPCIONES : ")
    print("1- Cargar archivo csv y mostrar ")
    print("2- asignar tiempos aleatoriamente y mostarlos ")
    print("3- informar el ganador")
    print("4- informa el promedio por tipo ")
    print("5- filtra por tipo ")
    print("6- exit ")
    
    return input (" ingrese el nro de opcion que desea : ")
   