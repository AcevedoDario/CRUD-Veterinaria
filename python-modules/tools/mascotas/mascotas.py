#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_mascotas():
    cleaning()
    print "-----------------------------".center(80, " ")
    print " MENÚ DE GESTIÓN DE MASCOTAS ".center(80, " ")
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

def ingresar_mascota(base):
    cleaning()
    print "------------------".center(80, " ")
    print " INGRESAR MASCOTA ".center(80, " ")
    print "------------------".center(80, " ")
    id_mascota = raw_input("\n\t\tIngrese el ID de la MASCOTA: ")
    id_mascota = validate_integer(id_mascota)
    if id_mascota not in base.keys():
        print "\n\tRellene los campos con la información correspondiente a la MASCOTA.\n"
        temporal = []
        dato = raw_input("\n\t\t1) Apellido(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t2) Nombre(s): ")
        temporal.append(dato)
        dato = raw_input("\n\t\t3) DNI del Propietario: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t4) Especie: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t5) Raza: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t6) Sexo: ")
        temporal.append(dato)
        dato = raw_input("\n\t\t7) Fecha de Nacimiento (dd/mm/aaaa): ")
        temporal.append(dato)
        base[id_mascota] = temporal
        cleaning()
        print "\n\t\tLa MASCOTA ha sido ingresado al SISTEMA exitosamente."
    else:
        print "\n\t\tLa MASCOTA que desea ingresar ya existe."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def modificar_mascota(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " MODIFICAR MASCOTA ".center(80, " ")
    print "-------------------".center(80, " ")
    id_mascota = raw_input("\n\t\tIngrese el ID del MASCOTA que desea modificar: ")
    id_mascota = validate_integer(id_mascota)
    cleaning()
    if id_mascota in base.keys():
        temporal = base[id_mascota]
        print "\nLos datos del MASCOTA N°", id_mascota, "a modificar son:\n"
        print "\n\t\t1) Apellido(s):", temporal[0]
        print "\n\t\t2) Nombre(s):", temporal[1]
        print "\n\t\t3) DNI del Propietario:", temporal[2] 
        print "\n\t\t4) Especie:", temporal[3] 
        print "\n\t\t5) Raza:", temporal[4] 
        print "\n\t\t6) Sexo:", temporal[5]
        print "\n\t\t7) Fecha de Nacimiento (dd/mm/aaaa):", temporal[6]
        print "\n\n\n\t\t8) Salir SIN MODIFICAR DATOS del MASCOTA."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 8)
        cleaning()
        if atributo <> 8:
            msje = "Ingrese "
            etiquetas = ["Apellido(s): ", "Nombre(s): ", "DNI del Propietario: ", "Especie: ", "Raza: ", "Sexo: ", "Fecha de Nacimiento (dd/mm/aaaa): "]
            msje = msje + etiquetas[atributo - 1]
            dato = raw_input(msje)
            temporal[atributo - 1] = dato
            base[id_mascota] = temporal
            cleaning()
            print "\n\t\tLa MASCOTA ha sido modificado en el SISTEMA exitosamente."
        else:
            print "\n\t\tNO ha sido modificado ningún atributo de la MASCOTA en el SISTEMA."    
    else:
        print "\nLa MASCOTA N°", id_mascota, "NO ESTÁ REGISTRADA.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_mascota(base):
    cleaning()
    print "----------------".center(80, " ")
    print " BUSCAR MASCOTA ".center(80, " ")
    print "----------------".center(80, " ")
    id_mascota = raw_input("\n\t\tIngrese el ID de la MASCOTA que desea buscar: ")
    id_mascota = validate_integer(id_mascota)
    cleaning()
    if id_mascota in base.keys():
        temporal = base[id_mascota]
        print "\nLos datos del MASCOTA buscado son:\n"
        print "\n\t\tMascota N°:", id_mascota
        print "\n\t\tApellido(s):", temporal[0]
        print "\n\t\tNombre(s):", temporal[1]
        print "\n\t\tDNI del propietario:", temporal[2] 
        print "\n\t\tEspecie:", temporal[3] 
        print "\n\t\tRaza:", temporal[4] 
        print "\n\t\tSexo:", temporal[5]
        print "\n\t\tFecha de Nacimiento (dd/mm/aaaa):", temporal[6]
    else:
        print "\nEl MASCOTA N°", id_mascota, "que desea buscar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_mascota(base):
    cleaning()
    print "------------------".center(80, " ")
    print " ELIMINAR MASCOTA ".center(80, " ")
    print "------------------".center(80, " ")
    id_mascota = raw_input("\n\t\tIngrese el ID de la MASCOTA que desea eliminar: ")
    id_mascota = validate_integer(id_mascota)
    cleaning()
    if id_mascota in base.keys():
        del base[id_mascota]
        cleaning()
        print "\n\t\tLa MASCOTA ha sido eliminado del SISTEMA exitosamente."
    else:
        print "\nLa MASCOTA N°", id_mascota, "NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")