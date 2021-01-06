#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_servicios():
    cleaning()
    print "---------------------------".center(80, " ")
    print " MENÚ GESTIÓN DE SERVICIOS ".center(80, " ")
    print "---------------------------".center(80, " ")
    print "\n\t1) Ingresar."
    print "\n\t2) Modificar."  
    print "\n\t3) Buscar."
    print "\n\t4) Eliminar."  
    print "\n\t5) Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion

def ingresar_servicio(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " INGRESAR SERVICIO ".center(80, " ")
    print "-------------------".center(80, " ")
    nombre_servicio = (raw_input("\n\t\tIngrese el NOMBRE del SERVICIO: ")).upper()
    if nombre_servicio not in base.keys():
        print "\n\tRellene los campos con la información correspondiente al SERVICIO.\n"
        temporal = []
        dato = raw_input("\n\t\t1) Apellido(s) del Especialista: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t2) Nombre(s) del Especialista: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t3) N° de Matricula del Especialista: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t4) Teléfono del Especialista: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t5) Dias de Atención: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t6) Horario de Atención: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t7) Costo del Servicio: ")
        temporal.append(dato)
        base[nombre_servicio] = temporal
        cleaning()
        print "\n\t\tEl SERVICIO ha sido ingresado al SISTEMA exitosamente."
    else:
        print "\n\t\tEl SERVICIO que desea ingresar ya existe."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def modificar_servicio(base):
    cleaning()
    print "--------------------".center(80, " ")
    print " MODIFICAR SERVICIO ".center(80, " ")
    print "--------------------".center(80, " ")
    nombre_servicio = (raw_input("\n\t\tIngrese el NOMBRE del SERVICIO que desea modificar: ")).upper()
    cleaning()
    if nombre_servicio in base.keys():
        temporal = base[nombre_servicio]
        print "\nLos datos del SERVICIO N°", nombre_servicio, "a modificar son:\n"
        print "\n\t\t1) Apellido(s) del Especialista:", temporal[0]
        print "\n\t\t2) Nombre(s) del Especialista:", temporal[1]
        print "\n\t\t3) N° de Matricula del Especialista:", temporal[2] 
        print "\n\t\t4) Teléfono del Especialista:", temporal[3] 
        print "\n\t\t5) Dias de Atención:", temporal[4] 
        print "\n\t\t6) Horario de Atención:", temporal[5] 
        print "\n\t\t7) Costo del Servicio:", temporal[6]
        print "\n\n\n\t\t8) Salir SIN MODIFICAR DATOS del SERVICIO."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 8)
        cleaning()
        if atributo <> 8:
            msje = "Ingrese "
            etiquetas = ["Apellido(s) del Especialista: ", "Nombre(s) del Especialista: ", "N° de Matricula del Especialista: ", "Teléfono del Especialista: ", "Dias de Atención: ", "Horario de Atención: ", "Costo del Servicio: "]
            msje = msje + etiquetas[atributo - 1]
            dato = raw_input(msje)
            temporal[atributo - 1] = dato
            base[nombre_servicio] = temporal
            cleaning()
            print "\n\t\tEl SERVICIO ha sido modificado en el SISTEMA exitosamente."
        else:
            print "\n\t\tNO ha sido modificado ningún atributo del SERVICIO en el SISTEMA."    
    else:
        print "\nEl SERVICIO N°", nombre_servicio, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_servicio(base):
    cleaning()
    print "-----------------".center(80, " ")
    print " BUSCAR SERVICIO ".center(80, " ")
    print "-----------------".center(80, " ")
    nombre_servicio = (raw_input("\n\t\tIngrese el NOMBRE del SERVICIO que desea buscar: ")).upper()
    cleaning()
    if nombre_servicio in base.keys():
        temporal = base[nombre_servicio]
        print "\nLos datos del SERVICIO buscado son:\n"
        print "\n\t\tServicio:", nombre_servicio
        print "\n\t\tApellido(s) del Especialista:", temporal[0]
        print "\n\t\tNombre(s) del Especialista:", temporal[1]
        print "\n\t\tN° de Matricula del Especialista:", temporal[2] 
        print "\n\t\tTeléfono del Especialista:", temporal[3] 
        print "\n\t\tDias de Atención:", temporal[4] 
        print "\n\t\tHorario de Atención:", temporal[5] 
        print "\n\t\tCosto del Servicio:", temporal[6] 
    else:
        print "\nEl SERVICIO de", nombre_servicio, ", NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_servicio(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " ELIMINAR SERVICIO ".center(80, " ")
    print "-------------------".center(80, " ")
    nombre_servicio = (raw_input("\n\t\tIngrese el NOMBRE del SERVICIO que desea eliminar: ")).upper()
    cleaning()
    if nombre_servicio in base.keys():
        del base[nombre_servicio]
        cleaning()
        print "\n\t\tEl SERVICIO ha sido eliminado del SISTEMA exitosamente."
    else:
        print "\nEl SERVICIO de", nombre_servicio, ", NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")