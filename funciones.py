import numpy
import time
import msvcrt
import os



estadio=numpy.zeros((10,10),int)

lista_rut=[]
lista_fila=[]
lista_asiento=[]

lista_total=[]

platinum=120000
gold=80000
silver=50000


def ver_menu():
    os.system("cls")
    print("""Menú
    1. Comprar Entradas
    2. Mostrar Ubicaciones Disponibles
    3. Ver Listado de Asistentes
    4. Mostrar Ganancias Totales
    5. Salir
    """)

def ver_estadio():
    print('''
     ____________________________
    |                            |
    |                            |
    |          ESCENARIO         |
    |                            |
    |____________________________|''')
    print()
    print("Asiento  1 2 3 4 5 6 7 8 9 10")
    for x in range(10):
        print(f"Fila {x+1}\t",end=" ")
        for i in range(10):
            print(estadio[x][i],end=" ")
        print()




def validar_opcion():
    while True:
        try:
            opcion=int(input("Ingrese la opción que desea: "))
            if opcion in (1,2,3,4,5):
                return opcion
            else:
                print("ERROR! DEBE INGRESAR UNA OPCIÓN ENTRE 1 Y 5")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def comprar_entrada():
    while True:
        try:
            entradas=int(input("Ingrese la cantidad de entradas que desea(Minimo 1, Maximo 3): "))
            if entradas in(1,2,3):
                return entradas
            else:
                print("ERROR! DEBE INGRESAR UNA CANTIDAD DE ENTRADAS MINIMO 1 Y MAXIMO 3")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def valor_entrada():
    print(f"""
    Valor Entrada Platinum: {platinum}
    Valor Entrada Gold: {gold}
    Valor Entrada Silver: {silver}
    """)

def validar_asiento():
    while True:
        ver_estadio()
        try:
            asiento=int(input("Ingrese el asiento que desea: "))
            if asiento in (1,2,3,4,5,6,7,8,9,10):
                return asiento
            else:
                print("ERROR! DEBE INGRESAR UN ASIENTO ENTRE 1 Y 10!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_fila():
    while True:
        ver_estadio()
        try:
            fila=int(input("Ingrese la fila que desea: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERROR! DEBE INGRESAR UNA FILA ENTRE 1 Y 10!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")




def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su Rut, sin puntos ni digito verificador: "))
            if rut>=1000000 and rut<=99999999:
                return rut
            else:
                print("ERROR! DEBE INGRESAR UN RUT ENTRE 1000000 y 99999999")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def comprar():
    while True:
        ver_estadio()
        valor_entrada()
        entradas=comprar_entrada()
        rut=validar_rut()
        lista_rut.append(rut)

        if 0 not in estadio:
            print("ENTRADAS AGOTADAS")
        else:
            for x in range(entradas):
                fila=validar_fila()
                asiento=validar_asiento()
                if estadio[fila-1][asiento-1]==0:
                    estadio[fila-1][asiento-1]=1
                    lista_fila.append(fila)
                    lista_asiento.append(asiento)
                    if fila in (1,2):
                        entradas=platinum
                        lista_total.append(entradas)
                    elif fila in (3,4,5):
                        entradas=gold
                        lista_total.append(entradas)
                    else:
                        entradas=silver
                        lista_total.append(entradas)
                    return
                
        print("ENTRADAS COMPRADAS CON EXITO")
        time.sleep(3)


def lista_asistentes():
    print(lista_rut)
    time.sleep(3)

def ganancias():
    print(f"""
    |Entradas           |Total
    |Platinum {platinum}|
    |Gold {gold}        |
    |Silver {silver}    |{lista_total}
    |""")
    print(lista_total)