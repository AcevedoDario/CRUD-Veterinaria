#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_clientes():
    cleaning()
    print "-----------------------------".center(80, " ")
    print " MENÚ DE GESTIÓN DE CLIENTES ".center(80, " ")
    print "-----------------------------".center(80, " ")
    print "\n\t1) Ingresar."
    print "\n\t2) Modificar."  
    print "\n\t3) Buscar."
    print "\n\t4) Eliminar."  
    print "\n\t5) Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion

def ingresar_cliente(base):
    cleaning()
    print "--------------------".center(80, " ")
    print " INGRESO DE CLIENTE ".center(80, " ")
    print "--------------------".center(80, " ")
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE: ")
    id_cliente = validate_integer(id_cliente)
    if id_cliente not in base.keys():
        print "\n\tRellene los campos con la información correspondiente al CLIENTE.\n"
        temporal = []
        dato = raw_input("\n\t\t1) Apellido(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t2) Nombre(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t3) Dirección: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t4) Código Postal: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t5) Localidad: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t6) Teléfono Fijo: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t7) Teléfono Celular: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t8) eMail: ")
        temporal.append(dato)
        base[id_cliente] = temporal
        cleaning()
        print "\n\t\tEl CLIENTE ha sido ingresado al SISTEMA exitosamente."
    else:
        print "\n\t\tEl CLIENTE que desea ingresar ya existe."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def modificar_cliente(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " MODIFICAR CLIENTE ".center(80, " ")
    print "-------------------".center(80, " ")
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea modificar: ")
    id_cliente = validate_integer(id_cliente)
    cleaning()
    if id_cliente in base.keys():
        temporal = base[id_cliente]
        print "\nLos datos del CLIENTE N°", id_cliente, "a modificar son:\n"
        print "\n\t\t1) Apellido(s):", temporal[0]
        print "\n\t\t2) Nombre(s):", temporal[1]
        print "\n\t\t3) Direccion:", temporal[2] 
        print "\n\t\t4) Código Postal:", temporal[3] 
        print "\n\t\t5) Localidad:", temporal[4] 
        print "\n\t\t6) Teléfono Fijo:", temporal[5] 
        print "\n\t\t7) Teléfono Celular:", temporal[6]
        print "\n\t\t8) eMail:", temporal[7]
        print "\n\n\n\t\t9) Salir SIN MODIFICAR DATOS del CLIENTE."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 9)
        cleaning()
        if atributo <> 9:
            msje = "Ingrese "
            etiquetas = ["Apellido(s): ", "Nombre(s): ", "Dirección: ", "Código Postal: ", "Localidad: ", "Teléfono Fijo: ", "Teléfono Celular: ", "eMail: "]
            msje = msje + etiquetas[atributo - 1]
            dato = raw_input(msje)
            temporal[atributo - 1] = dato
            base[id_cliente] = temporal
            cleaning()
            print "\n\t\tEl CLIENTE ha sido modificado en el SISTEMA exitosamente."
        else:
            print "\n\t\tNO ha sido modificado ningún atributo del CLIENTE en el SISTEMA."    
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_cliente(base):
    cleaning()
    print "----------------".center(80, " ")
    print " BUSCAR CLIENTE ".center(80, " ")
    print "----------------".center(80, " ")
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea buscar: ")
    id_cliente = validate_integer(id_cliente)
    cleaning()
    if id_cliente in base.keys():
        temporal = base[id_cliente]
        print "\nLos datos del CLIENTE buscado son:\n"
        print "\n\t\tCliente N°:", id_cliente
        print "\n\t\tApellido(s):", temporal[0]
        print "\n\t\tNombre(s):", temporal[1]
        print "\n\t\tDireccion:", temporal[2] 
        print "\n\t\tCódigo Postal:", temporal[3] 
        print "\n\t\tLocalidad:", temporal[4] 
        print "\n\t\tTeléfono Fijo:", temporal[5] 
        print "\n\t\tTeléfono Celular:", temporal[6]
        print "\n\t\teMail:", temporal[7]  
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea buscar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_cliente(base):
    cleaning()
    print "------------------".center(80, " ")
    print " ELIMINAR CLIENTE ".center(80, " ")
    print "------------------".center(80, " ")
    id_cliente = raw_input("\n\t\tIngrese el DNI del CLIENTE que desea eliminar: ")
    id_cliente = validate_integer(id_cliente)
    cleaning()
    if id_cliente in base.keys():
        del base[id_cliente]
        cleaning()
        print "\n\t\tEl CLIENTE ha sido eliminado del SISTEMA exitosamente."
    else:
        print "\nEl CLIENTE N°", id_cliente, "que desea eliminar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")