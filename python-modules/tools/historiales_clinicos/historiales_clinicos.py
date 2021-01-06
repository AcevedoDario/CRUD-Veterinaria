#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_historial_clinico():
    cleaning()
    print "------------------------------".center(80, " ")
    print " MENÚ DE HISTORIALES CLÍNICOS ".center(80, " ")
    print "------------------------------".center(80, " ")
    print "\n\t1) Ingresar."
    print "\n\t2) Buscar."
    print "\n\t3) Eliminar."
    print "\n\t4) Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 4)
    return opcion

def ingresar_historia_clinica(base, base2):
    cleaning()
    print "---------------------------".center(80, " ")
    print " INGRESAR HISTORIA CLÍNICA ".center(80, " ")
    print "---------------------------".center(80, " ")
    id_historia = raw_input("\n\t\tIngrese el ID de la MASCOTA con historia clínica: ")
    id_historia = validate_integer(id_historia)
    if id_historia in base2.keys():
        dato = raw_input("\n\t\tIngrese Informe Clínico: \n\n")
        temporal = []
        temporal.append(dato)
        if id_historia in base.keys():
            base[id_historia].append(dato)
        else:
            base[id_historia] = temporal
        cleaning()
        print "\n\t\tEl HISTORIAL CLÍNICO ha sido ingresado al SISTEMA exitosamente."
    else:
		print "\n\t\tLa MASCOTA con ID N°", id_historia,"NO ESTÁ REGISTRADO."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_historia_clinica(base):
    cleaning()
    print "--------------------------".center(80, " ")
    print " BUSCAR HISTORIAL CLÍNICO ".center(80, " ")
    print "--------------------------".center(80, " ")
    id_historia = raw_input("\n\t\tIngrese el ID de la MASCOTA con HISTORIAL CLÍNICO que desea buscar: ")
    id_historia = validate_integer(id_historia)
    cleaning()
    if id_historia in base.keys():
        elemento = 0
        historial = base[id_historia]
        print "HISTORIAL CLÍNICO de la mascota".center(50, " "), id_historia.center(50, " ")
        while elemento <= (len(historial) - 1):
            print base[id_historia][elemento]
            elemento = elemento + 1
            print "\n\n"
    else:
        print "\nEl HISTORIAL CLINICO de la mascota N°", id_historia, "NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_historia_clinica(base):
    cleaning()
    print "----------------------------".center(80, " ")
    print " ELIMINAR HISTORIAL CLÍNICO ".center(80, " ")
    print "----------------------------".center(80, " ")
    id_historia = raw_input("\n\t\tIngrese el ID de la MASCOTA con HISTORIAL CLÍNICO que desea eliminar: ")
    id_historia = validate_integer(id_historia)
    cleaning()
    if id_historia in base.keys():
        del base[id_historia]
        cleaning()
        print "\n\t\tEl HISTORIAL CLÍNICO de la MASCOTA N°", id_historia, " ha sido eliminada del SISTEMA exitosamente."
    else:
        print "\nEl HISTORIAL CLÍNICO de la mascota N°", id_historia, "NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")