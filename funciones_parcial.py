from os import system
import csv
import random
import os




def get_path_actual(nombre_archivo):
    """_summary_

    Args:
        nombre_archivo (_type_): Nombre del archivo actual

    Returns:
        _type_: la ubicacion del archivo en el que se trabaja
    """
    
    ubi = os.path.dirname(__file__)
    
    return os.path.join(ubi, nombre_archivo)

# ----------------------------------------------------------------
def cargar_archivo_csv(nombre_archivo_data:str, lista):
    """_summary_

    Args:
        nombre_archivo_data (str): Nombre del archivo de donde se obtendra la informacion
    """
    with open(get_path_actual(nombre_archivo_data), "r", encoding="utf-8") as archivo:
         encabezado = archivo.readline().strip("\n").split(",")
    
         for linea in archivo.readlines():
            bicicleta = {}
            linea = linea.strip("\n").split(",")
            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = tiempo
            
            lista.append(bicicleta)
            

# -----------------------------

def mostrar_ciclistas_tabla(lista:list):
    tam = len(lista)
    print("                      LISTA DE CICLISTAS")
    print("ID     Nombre            Tipo        Tiempo")
    print("------------------------------------------------------------------------")
    for ciclista in lista:
        print(f"{ciclista["id_bike"]}    {ciclista["nombre"]:15}    {ciclista["tipo"]:10}    {ciclista["tiempo"]}")

def numeros_ramdom(lista):
    lista["tiempo"] = random.randint(50,120)
    return lista
# ----------------------------------------------------------------

def mapear_lista(funcion, lista:list)->list:
    """_summary_

    Args:
        funcion (_type_): Funcion para mapear
        lista (list): Lista que se va a mapear

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste y con lo que especifiques en la funcion,
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno

# ----------------------------------------------------------------
def calcular_menor(lista: list) -> int:
    """
    Calcula el menor elemento de una lista.

    Args:
        lista (list): Lista de elementos numéricos.

    Raises:
        ValueError: Si la lista está vacía.

    Returns:
        int: El menor elemento de la lista.
    """
    if len(lista) == 0:
        raise ValueError("No está definido el menor de una lista vacía")
    
    flag_primer_elemento = True
    for elemento in lista:
        if flag_primer_elemento or menor > elemento:
            flag_primer_elemento = False
            menor = elemento

    return menor
# ----------------------------------------------------------------

def definir_campo(campo: str) -> str:
    """
    Define el campo de la lista basado en un alias corto.

    Args:
        campo (str): Alias del campo a evaluar.

    Raises:
        ValueError: Si no se ingresa un valor válido.

    Returns:
        str: El nombre completo del campo.
    """
    match campo:
        case "n":
            retorno = "nombre"
        case "id":
            retorno = "id_bike"
        case "tipe":
            retorno = "tipo"
        case "time":
            retorno = "tiempo"
        case _: 
            raise ValueError("No es un campo válido")
    return retorno
# ----------------------------------------------
def swap_lista(lista:list, valor1, valor2):
    """swap

    Args:
        lista (list): lista a swapear
        valor1 (_type_): primer valor a swapear
        valor2 (_type_): segundo valor a swapear
    """
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux
#------------------------------------------
def ordenar_campo(lista: list, campo: str, asc: bool = True):
    """
    Ordena una lista según un campo específico y en orden ascendente o descendente.

    Args:
        lista (list): Lista a ordenar.
        campo (str): Campo a ordenar.
        asc (bool, optional): True para orden ascendente, False para descendente. Defaults to True.

    Raises:
        ValueError: Si no se ingresa una lista.
    """
    if isinstance(lista, list):
        atributo = definir_campo(campo)
        tam = len(lista)
        for i in range(tam - 1):
            for j in range(i + 1, tam):
                if (lista[i][atributo] > lista[j][atributo]) if asc else (lista[i][atributo] < lista[j][atributo]):
                    swap_lista(lista, i, j)
    else:
        raise ValueError("No se ingresó ninguna lista")
#------------------------------------------
def asignar_ganador(lista: list):
    """
    Recorre la lista y asigna el ganador basado en el menor tiempo.

    Args:
        lista (list): Lista de ciclistas.

    Returns:
        list: Lista de ganadores.
    """
    ganador = []
    ordenar_campo(lista, "time", True)
    for i in lista:
        if i["tiempo"] == lista[0]["tiempo"]:
            ganador.append(i)
    return ganador
    
# ------------------------------------------
def filtrar_lista(funcion, lista:list)->list:
    """filtra una lista segun la funcion

    Args:
        funcion (_type_): Funcion para filtrar
        lista (list): Lista que se va a filtrar

    Returns:
        list: lista filtrada segun funcion
    """
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

# ----------------------------------------------------------------




def crear_archivo_tipo(lista:list):
    """crea un archivo csv con la lista que pasa por parametro

    Args:
        lista (list): lista con datos para crear archivo
    """
    
    tipe_bike = input("Ingrese el tipo de bicicleta ").upper()

    
    while tipe_bike != "BMX" and tipe_bike != "PLAYERA" and tipe_bike != "MTB" and tipe_bike != "PASEO":
        tipe_bike = input("Ingrese un tipo de bicicleta valido: ")
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == tipe_bike, lista))
    
    
    with open(get_path_actual(tipe_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            l = ",".join(lista_tipo[i]) + "\n"
    
        for persona in lista_tipo:
            values = list(persona.values())
            l = []
            for value in values:
                if isinstance(value,int):
                    l.append(str(value))
                elif isinstance(value,float):
                    l.append(str(value))
                else:
                    l.append(value)
            linea = ",".join(l) + "\n"
            archivo.write(linea)

# ----------------------------------------------------------------

def totalizar_lista(lista:list)->int:
    """totaliza una lista

    Args:
        lista (list): lista a sumar

    Raises:
        ValueError: no es lista

    Returns:
        int: Suma todos sus elementos
    """
    if  isinstance(lista, list):
        total = 0
        for el in lista:
            total += int(el)
        return total
    else:
        raise ValueError("No se ingreso ninguna lista") 

# ----------------------------------------------------------------


def calcular_promedio(lista:list)->int:
    """promedia una lista

    Args:
        lista (list): lista a calcular promedio

    Raises:
        ValueError: lista vacia
        ValueError: No es una lista

    Returns:
        float: El promedio  de la lista
    """
    if  isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return round(totalizar_lista(lista) / cant)
    else:
        raise ValueError("No se ingreso ninguna lista") 
    
# ----------------------------------------------------------------

def ordenar_por_dos_campos(lista:list, campo_uno:str, campo_dos:str):
    """
    Ordena una lista ascendente.

    Args:
        bicicletas (list): Lista de diccionarioss.
        campo_tipo (str): Nombre del campo uno.
        campo_tiempo (str): Nombre del campo 2.
    """
    tam = len(lista)
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if lista[i][campo_uno] == lista[j][campo_uno]:
                if lista[i][campo_dos] < lista[j][campo_dos]:
                    lista[i], lista[j] = lista[j], lista[i]
            elif lista[i][campo_uno] < lista[j][campo_uno]:
                lista[i], lista[j] = lista[j], lista[i]

# ----------------------------------------------------------------
    

def limpiar_pantalla ():
    """limpia la pantalla

    Returns:
        _type_: limpia la terminal
    """
    return system ("cls")
# ----------------------------------------------------------------

def pausar ():
    """_summary_

    Returns:
        _type_: pausa el sistema en cada iteracion
    """
    return system("pause")
# ----------------------------------------------------------------

def menu():
    """crea un menu

    Returns:
        _type_: ingresa la opcion del menu
    """
    limpiar_pantalla()
    print("   MENU DE OPCIONES : ")
    print("1- Cargar archivo csv")
    print("2- mostar archivo ")
    print("3- cargar tiempos")
    print("4- informar ganador ")
    print("5- filtra por tipo y crea un archivo del tipo seleccionado ")
    print("6- muestra el promedio por tipo ")
    print("7- muestra las posiciones  ")
    print("8- guarda las posiciones en archivos JSON  ")
    print("9- salir del programa  ")
    
    
    return input (" ingrese el nro de opcion que desea : ")
   