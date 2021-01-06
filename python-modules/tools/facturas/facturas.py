#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_facturacion():
    cleaning()
    print "---------------------".center(80, " ")
    print " Menú de FACTURACION ".center(80, " ")
    print "---------------------".center(80, " ")
    print "\n\t1) Crear FACTURA."
    print "\n\t2) Consultar FACTURA."  
    print "\n\t3) Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 3)
    return opcion

def crear_factura(base1, base2, base3):
    cleaning()
    flag = True
    temporal_nombre = []
    temporal_precios = []
    item = 0
    factura = 1
    total = 0
    while factura in base3.keys():
        factura = factura + 1
    while flag == True:
        print "--------------------------------".center(80, " ")
        print " FACTURAR PRODUCTOS Y SERVICIOS ".center(80, " ")
        print "--------------------------------".center(80, " ")
        elemento = (raw_input("\n\n\tIngrese el CODIGO/NOMBRE del PRODUCTO/SERVICIO que va a facturar:\n\n\n\n\t\t\t\t\t")).upper()
        if elemento in base1.keys() or elemento in base2.keys():
            if elemento in base1.keys():
                temporal_nombre.append(base1[elemento][0])
                temporal_precios.append(base1[elemento][3])
                print "\n\t\tEl PRODUCTO se ha agregado a la factura exitosamente."
                raw_input("\n\n\t\t\tPresione la tecla ENTER para continuar.")
            else:
                temporal_nombre.append(elemento)
                temporal_precios.append(base2[elemento][6])
                print "\n\t\tEl SERVICIO se ha agregado a la factura exitosamente."
                raw_input("\n\n\t\t\tPresione la tecla ENTER para continuar.")
        else:
            print "\n\t\tEl PRODUCTO/SERVICIO que desea agregar a la factura NO ESTÁ REGISTRADO."
            raw_input("\n\n\t\t\tPresione la tecla ENTER para continuar.")
        cleaning()
        print "Desea agregar otro PRODUCTO/SERVICIO a la factura?".center(80, " ")
        print "\n\t1) Si."
        print "\n\t2) No."
        opcion = raw_input("\n\n\t\tIngrese una opción: ")
        opcion = validate_integer(opcion)
        opcion = validate_range(opcion, 1, 2)
        cleaning()
        if opcion == 2:
            flag = False
            temporal_elemento =(temporal_nombre, temporal_precios)
            base3[factura] = temporal_elemento
            cleaning()
    print ("FACTURA N°" + str(factura)).center(80, " ")
    while flag == False:
        if item < len(temporal_nombre):
            print str(temporal_nombre[item]).ljust(20, " ") + ">  $".rjust(20, "-") + str(temporal_precios[item]).rjust(4, " ")
            total = total + int(temporal_precios[item])
            item = item + 1
        else:
            print "_".center(80, "_") + "\nTOTAL".ljust(21, " ") + ">  $".rjust(20, "-") + str(total).rjust(4, " ")
            flag = True
    raw_input("\n\n\t\t\tPresione la tecla ENTER para continuar.")

def consultar_factura(base):
    cleaning()
    total = 0
    print "-------------------".center(80, " ")
    print " CONSULTAR FACTURA      ".center(80, " ")
    print "-------------------".center(80, " ")
    factura = int(raw_input("\n\n\t\tIngrese el NUMERO de FACTURA que desea consultar.\n"))
    cleaning()
    if factura in base.keys():
        print ("FACTURA N°" + str(factura)).center(80, " ")
        for item in range (len(base[factura][0])):
            print str(base[factura][0][item]).ljust(20, " ") + ">  $".rjust(20, "-") + str(base[factura][1][item])
            total = total + int(base[factura][1][item])
        print "_".center(80, "_") + "\nTOTAL".ljust(21, " ") + ">  $".rjust(20, "-") + str(total).rjust(3, " ")
    else:
        print "\n\t\tEl NUMERO de FACTURA que desea consultar NO ESTÁ REGISTRADO."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")