#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")

from tools.validate.validate import *
from tools.view.view import *

def menu_productos():
    cleaning()
    print "------------------------------".center(80, " ")
    print " MENÚ DE GESTIÓN DE PRODUCTOS ".center(80, " ")
    print "------------------------------".center(80, " ")
    print "\n\t1) Ingresar."
    print "\n\t2) Modificar."  
    print "\n\t3) Buscar."
    print "\n\t4) Eliminar."  
    print "\n\t5) Retornar al Menú Principal."
    opcion = raw_input("\n\n\t\tIngrese una opción: ")
    opcion = validate_integer(opcion)
    opcion = validate_range(opcion, 1, 5)
    return opcion

def ingresar_producto(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " INGRESAR PRODUCTO ".center(80, " ")
    print "-------------------".center(80, " ")
    id_producto = raw_input("\n\t\tIngrese el CODIGO del PRODUCTO: ")
    if id_producto not in base.keys():
        print "\n\tRellene los campos con la información correspondiente al PRODUCTO.\n"
        temporal = []
        dato = (raw_input("\n\t\t1) Nombre: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t2) Descripcion: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t3) Unidades: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t4) Precio de Venta: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t5) Proveedor: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t6) Teléfono Proveedor: ")).upper()
        temporal.append(dato)
        dato = (raw_input("\n\t\t7) Email Proveedor: ")).upper()
        temporal.append(dato)
        base[id_producto] = temporal
        cleaning()
        print "\n\t\tEl PRODUCTO ha sido ingresado al SISTEMA exitosamente."
    else:
        print "\n\t\tEl PRODUCTO que desea ingresar ya existe."
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def modificar_producto(base):
    cleaning()
    print "--------------------".center(80, " ")
    print " MODIFICAR PRODUCTO ".center(80, " ")
    print "--------------------".center(80, " ")
    id_producto = raw_input("\n\t\tIngrese el CODIGO del PRODUCTO que desea modificar: ")
    cleaning()
    if id_producto in base.keys():
        temporal = base[id_producto]
        print "\nLos datos del PRODUCTO N°", id_producto, "a modificar son:\n"
        print "\n\t\t1) Nombre:", temporal[0]
        print "\n\t\t2) Descripcion:", temporal[1]
        print "\n\t\t3) Unidades:", temporal[2] 
        print "\n\t\t4) Precio de Venta:", temporal[3] 
        print "\n\t\t5) Proveedor:", temporal[4] 
        print "\n\t\t6) Teléfono Proveedor:", temporal[5] 
        print "\n\t\t7) Email Proveedor:", temporal[6]
        print "\n\n\n\t\t8) Salir SIN MODIFICAR DATOS del PRODUCTO."
        atributo = raw_input("\n\n\t\tIngrese una opción: ")
        atributo = validate_integer(atributo)
        atributo = validate_range(atributo, 1, 8)
        cleaning()
        if atributo <> 8:
            msje = "Ingrese "
            etiquetas = ["Nombre: ", "Descripcion: ", "Unidades: ", "Precio de Venta: ", "Proveedor: ", "Teléfono Proveedor: ", "Email Proveedor: "]
            msje = msje + etiquetas[atributo - 1]
            dato = (raw_input(msje)).upper()
            temporal[atributo - 1] = dato
            base[id_producto] = temporal
            cleaning()
            print "\n\t\tEl PRODUCTO ha sido modificado en el SISTEMA exitosamente."
        else:
            print "\n\t\tNO ha sido modificado ningún atributo del PRODUCTO en el SISTEMA."    
    else:
        print "\nEl PRODUCTO N°", id_producto, "que desea modificar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def buscar_producto(base):
    cleaning()
    print "-----------------".center(80, " ")
    print " BUSCAR PRODUCTO ".center(80, " ")
    print "-----------------".center(80, " ")
    id_producto = raw_input("\n\t\tIngrese el CODIGO del PRODUCTO que desea buscar: ")
    cleaning()
    if id_producto in base.keys():
        temporal = base[id_producto]
        print "\nLos datos del PRODUCTO buscado son:\n"
        print "\n\t\tProducto N°:", id_producto
        print "\n\t\tNombre:", temporal[0]
        print "\n\t\tDescripcion:", temporal[1]
        print "\n\t\tUnidades:", temporal[2] 
        print "\n\t\tPrecio de Venta:", temporal[3] 
        print "\n\t\tProveedor:", temporal[4] 
        print "\n\t\tTeléfono Proveedor:", temporal[5] 
        print "\n\t\tEmail Proveedor:", temporal[6] 
    else:
        print "\nEl PRODUCTO N°", id_producto, "que desea buscar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")

def eliminar_producto(base):
    cleaning()
    print "-------------------".center(80, " ")
    print " ELIMINAR PRODUCTO ".center(80, " ")
    print "-------------------".center(80, " ")
    id_producto = raw_input("\n\t\tIngrese el CODIGO del PRODUCTO que desea eliminar: ")
    cleaning()
    if id_producto in base.keys():
        del base[id_producto]
        cleaning()
        print "\n\t\tEl PRODUCTO ha sido eliminado del SISTEMA exitosamente."
    else:
        print "\nEl PRODUCTO N°", id_producto, "que desea eliminar, NO ESTÁ REGISTRADO.\n"
    raw_input("\n\n\t\t\t\tPresione la tecla ENTER para continuar.")