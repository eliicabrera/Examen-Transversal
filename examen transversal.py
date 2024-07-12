import csv
import random
#VARIABLES
empresa = []
sueldos = []
trabajadores = ["María García","Carlos López","Ana Martínez","Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Abel Gómez","Francisco Díaz"]

#FUNCIONES
def imprimir_menu():
    print("**************")
    print("*MENÚ EMPRESA*")
    print("**************")
    print("[1]Asignar sueldos aleatorios")
    print("[2]Clasificar sueldos")
    print("[3]Ver estadisticas")
    print("[4]SALIR")

def obtener_opc():
    while True:
        try:
            opc = int(input("Ingrese una opción[1-4]:\n"))
            if opc >=1 and opc <=4:
                      return opc
            else:
                print("ERROR. Ingrese opción válida dentro del rango [1-4]")
        except:
            print("ERROR. Ingrese un valor númerico")
        
def generar_archivo():
    try:
        open('archivo.csv', 'x')
    except:
        print("archivo.cvs ya está creado!")

def generar_sueldos(sueldos):
    while True:
                try:
                    num = int(input("Ingrese un número del 1 al 5: "))
                    if num >= 1 and num <= 5:
                        print()
                        if num == 1:
                            print ("Los sueldos al azar son:")
                            sueldos = ['300000','350000','400000','600000','750000','870000','560000','1700000','2000000','2300000']
                            for sueldo in sueldos:
                                print (f"{sueldo}", end=" ")
                                pass
                            break
                        if num == 2:
                            print ("Los sueldos al azar son:")
                            sueldos = ['350000','500000','470000','650000','780000','890000','570000','1300000','1700000','2100000']
                            for sueldo in sueldos:
                                print (f"{sueldo}", end=" ")
                                pass
                            break
                        if num == 3:
                            print ("Los sueldos al azar son:")
                            sueldos = ['420000','450000','760000','610000','770000','900000','660000','1300000','2100000','2200000']
                            for sueldo in sueldos:
                                print (f"{sueldo}", end=" ")
                                pass
                            break
                        if num == 4:
                            print ("Los sueldos al azar son:")
                            sueldos = ['700000','450000','480000','690000','790000','870000','590000','1200000','1500000','2440000']
                            for sueldo in sueldos:
                                print (f"{sueldo}", end=" ")
                                pass
                            break
                        if num == 5:
                            print ("Los sueldos al azar son:")
                            sueldos = ['490000','500000','459000','692000','749000','810000','520000','1450000','2200000','2330000']
                            for sueldo in sueldos:
                                print (f"{sueldo}", end=" ")
                                pass
                            break
                    else:
                        print("ERROR. Ingrese número en el rango[1-5]")
                except:
                    print("ERROR. Ingrese un carácter válido")
            
#??????????????
#for i in sueldos:
#sueldoazar = i.random(300000,2500000)
#print(sueldoazar)
#sueldos.append(sueldoazar)
                    
while True:    
    imprimir_menu()
    opc = obtener_opc()
    if opc == 1:
        sueldos = generar_sueldos(sueldos)
        input("\nPresione enter para continuar -->")
    if opc == 2:
        empresa = []
        empresa.append(trabajadores)
        empresa.append(sueldos)
        print(empresa)
        input("Presione enter para continuar -->")
    if opc == 3:
        print()
    if opc == 4:
        generar_archivo()
        print()
    if opc == 5:
        print("""Saliendo del programa...
              Desarrollado por Eli Cabrera
              RUT 21.622.093-5""")
        break
            


