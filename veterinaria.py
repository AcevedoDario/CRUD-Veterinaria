#coding=UTF-8


import sys
import pickle

sys.path.append("python-modules")


from tools.clientes.clientes import *
from tools.facturas.facturas import *
from tools.mascotas.mascotas import *
from tools.historiales_clinicos.historiales_clinicos import *
from tools.servicios.servicios import *
from tools.productos.productos import *


validating_existence_file("clientes.dat")
validating_existence_file("facturas.dat")
validating_existence_file("mascotas.dat")
validating_existence_file("historial_clinico.dat")
validating_existence_file("servicios.dat")
validating_existence_file("productos.dat")


clientes = {}
facturas = {}
mascotas = {}
historial_clinico = {}
servicios = {}
productos = {}


def menu_principal():
	cleaning()
	print "--------------------------------".center(80, " ")
	print " SISTEMA DE CLINICA VETERINARIA ".center(80, " ")
	print "--------------------------------".center(80, " ")
	print "Menú Principal."
	print "\n\t1) Clientes."
	print "\n\t2) Mascotas."
	print "\n\t3) Historias Clinicas."
	print "\n\t4) Productos."
	print "\n\t5) Servicios."
	print "\n\t6) Facturacion."
	print "\n\t7) Salir."
	opcion = raw_input("\n\n\t\tIngrese una opción: ")
	opcion = validate_integer(opcion)
	opcion = validate_range(opcion, 1, 7)
	return opcion


#Programa principal
seleccion = menu_principal()
while seleccion <> 7:
    if seleccion == 1:
        #Cargando los datos del archivo "clientes.dat" al diccionario clientes
        clientes = loading_file_into_memory("clientes.dat")
        seleccion = menu_clientes()
        while seleccion <> 5:
            if seleccion == 1:
                ingresar_cliente(clientes)
            elif seleccion == 2:
                modificar_cliente(clientes)
            elif seleccion == 3:
                buscar_cliente(clientes)
            else:
                eliminar_cliente(clientes)
            seleccion = menu_clientes()
		#Guardando los cambios del diccionario clientes al archivo "clientes.dat"
        saving_changes_to_the_file("clientes.dat", clientes)
    elif seleccion == 2:
		#Cargando los datos del archivo "mascotas.dat" al diccionario mascotas
		mascotas = loading_file_into_memory("mascotas.dat")
		seleccion = menu_mascotas()
		while seleccion <> 5:
			if seleccion == 1:
				ingresar_mascota(mascotas)
			elif seleccion == 2:
				modificar_mascota(mascotas)
			elif seleccion == 3:
				buscar_mascota(mascotas)
			else:
				eliminar_mascota(mascotas)
			seleccion = menu_mascotas()
		#Guardando los cambios del diccionario mascotas al archivo "mascotas.dat"
		saving_changes_to_the_file("mascotas.dat", mascotas)
    elif seleccion == 3:
        #Cargando los datos del archivo "mascotas.dat" al diccionario mascotas y los datos del archivo "historial_clinico.dat" al diccionario historial_clinico
        mascotas = loading_file_into_memory("mascotas.dat")
        historial_clinico = loading_file_into_memory("historial_clinico.dat")
        seleccion = menu_historial_clinico()
        while seleccion <> 4:
            if seleccion == 1:
                ingresar_historia_clinica(historial_clinico, mascotas)
            elif seleccion == 2:
                buscar_historia_clinica(historial_clinico)
            else:
                eliminar_historia_clinica(historial_clinico)
            seleccion = menu_historial_clinico()
        #Guardando los cambios del diccionario historial_clinico al archivo "historial_clinico.dat"
        saving_changes_to_the_file("historial_clinico.dat", historial_clinico)
    elif seleccion == 4:
        #Cargando los datos del archivo "productos.dat" al diccionario productos
        productos = loading_file_into_memory("productos.dat")
        seleccion = menu_productos()
        while seleccion <> 5:
            if seleccion == 1:
                ingresar_producto(productos)
            elif seleccion == 2:
                modificar_producto(productos)
            elif seleccion == 3:
                buscar_producto(productos)
            else:
                eliminar_producto(productos)
            seleccion = menu_productos()
        #Guardando los cambios del diccionario productos al archivo "productos.dat"
        saving_changes_to_the_file("productos.dat", productos)        
    elif seleccion == 5:
        #Cargando los datos del archivo "servicios.dat" al diccionario servicios
        servicios = loading_file_into_memory("servicios.dat")
        seleccion = menu_servicios()
        while seleccion <> 5:
            if seleccion == 1:
                ingresar_servicio(servicios)
            elif seleccion == 2:
                modificar_servicio(servicios)
            elif seleccion == 3:
                buscar_servicio(servicios)
            else:
                eliminar_servicio(servicios)
            seleccion = menu_servicios()
        #Guardando los cambios del diccionario servicios al archivo "servicios.dat"
        saving_changes_to_the_file("servicios.dat", servicios)
    else:
        #Cargando los datos del archivo "productos.dat" al diccionario productos
        productos = loading_file_into_memory("productos.dat")
        #Cargando los datos del archivo "servicios.dat" al diccionario servicios
        servicios = loading_file_into_memory("servicios.dat")
        #Cargando los datos del archivo "facturas.dat" al diccionario facturas
        facturas = loading_file_into_memory("facturas.dat")
        seleccion = menu_facturacion()
        while seleccion <> 3:
            if seleccion == 1:
                crear_factura(productos, servicios, facturas)
            else:
                consultar_factura(facturas)
            seleccion = menu_facturacion()
        #Guardando los cambios del diccionario facturas al archivo "facturas.dat"
        saving_changes_to_the_file("facturas.dat", facturas)
    seleccion = menu_principal()
cleaning()
raw_input("\n\tUsted ha salido exitosamente del SISTEMA.\n\n\t\t\tPresione la tecla ENTER para terminar de salir.")
cleaning()