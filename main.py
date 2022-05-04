# Formato: ID del producto, Nombre del producto, Precio del producto, Cantidad del producto en el inventario
from ctypes import alignment
from tkinter import CENTER
from turtle import title
from Funciones import *
from LecturaArchivoTexto import productos
from Queue import *
from LinkedList import *
from HeapSort import sort
from rich.theme import Theme
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import cProfile 

#cProfile.run('foo()')

cont=0
productos_carrito=[]


custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

opcion = 0
opcion1 = 0
opcion2 = 0
cabeza = 0
cont = 0
acu = 1
tot = 0
ids = []
pagos = []
opcioncompra = 0
usuario = "admin"
contra = "contrasena"

while (opcion != 3):
    #Menu inicial para elegir la opcion de compra o la de inventario
    table = Table(title="MENU PRINCIPAL", style="bold")
    table.add_column("No.", style="bold")
    table.add_column("Opcion", style="bold")

    table.add_row("1.", "Comprar")
    table.add_row("2.", "Administrar inventario (requiere autenticación)")
    table.add_row("3.", "Salir")
    console.print(table)

    #print('Ingrese que operación desea realizar \n')
    #print('1. Comprar')
    #print('2. Administrar inventario (requiere autenticación)')
    #print('3. Salir')

    try:
        opcion = int(input("\n"))
    except:
        console.print('Error', style="error")
    else:

        if opcion == 1:
            opcioncompra=10
            while opcioncompra != 5:
                if cont == 0:
                    cabeza = 0
                print('\n')
                #Menu de la opcion de compra
                table_compra = Table(title="MENU DE COMPRA", style="bold")

                table_compra.add_column("No.", style="bold") 
                table_compra.add_column("Opcion", style="bold") 

                table_compra.add_row("1.", "Agregar productos al carrito")
                table_compra.add_row("2.", "Eliminar productos del carrito")
                table_compra.add_row("3.", "Mostrar carrito")
                table_compra.add_row("4.", "Checkout")
                table_compra.add_row("5.", "Salir")
                console.print(table_compra)
                
                #print('1. Agregar productos al carrito')
                #print('2. Eliminar productos del carrito')
                #print('3. Mostrar carreta')
                #print('4. Checkout')
                #print('5. Salir')
                try:
                    opcioncompra = int(input('Ingrese la opción que desea realizar: \n', ))
                except:
                    print('Ingrese un numero:')


                if (opcioncompra == 1):
                    namecompra = ''
                    #Muestra de nuestros productos disponibles
                    while namecompra == '':
                        table_productos_dispo = Table(title='Productos disponibles')
                        
                        table_productos_dispo.add_column("item_name", style="bold")
                        table_productos_dispo.add_column("precio", style="bold")
                        table_productos_dispo.add_column("cantidad", style="bold")
                        table_productos_dispo.add_column("caducidad", style="bold")
                        for x in productos:
                            table_productos_dispo.add_row(x["item_name"], str(x["precio"]), str(x["cantidad"]), str(x["caducidad"]))
                        console.print(table_productos_dispo)
                            
                        #Solicitar que ingrese el NOMBRE del producto que desea ingresar
                        namecompra = (input("\n Ingrese el nombre del producto a comprar\n"))
                        try:
                            #Solicitar la cantidad que desea
                            cantidadcompra = int(input('Ingrese la cantidad del producto a comprar\n'))
                                
                        except:
                            console.print('Error', style="error")
                        else:
                            #Verifica que ingrese una cantidad positiva
                            if (positivo(cantidadcompra) == 1):
                                #Verifica la existencia del producto
                                seccion = search_name(namecompra, productos)
                                if (seccion == 0):
                                    console.print('Ingrese el nombre de un producto existente:', style="bold")
                                else:
                                    #Verifica la cantidad de existencia del producto
                                    if (verify_name(namecompra, cantidadcompra, productos) == 0):
                                        console.print('No existe la cantidad suficiente de productos', style="error")
                                    else:
                                        #Verifica si el carrito este vacio
                                        if cabeza == 0:
                                            checkout = 1
                                            items_comprados = SinglyLinkedList(Node(namecompra))
                                            for i in range(2, 50):
                                                #Agrega el producto a la LinkedList
                                                items_comprados.insert(i, i - 1, items_comprados)
                                            cabeza = 1
                                            cont = cont + 1
                                            #Resta la cantidad del inventario
                                            rest_cantidad(verify_name(namecompra,cantidadcompra, productos), cantidadcompra, productos)
                                            #Agrega el producto al carrito
                                            productos_carrito.append({'item_name':namecompra,'cantidad':cantidadcompra})
                                            #Agrega el pago
                                            pagos.append(total(namecompra,cantidadcompra,productos))
                                        else:
                                            #Verifica si el producto ya se encuentra en el carrito
                                            if (search_carrito(namecompra, productos_carrito) == 1):
                                                console.print('Este producto ya se encuentra en el carrito', style="success")
                                            else:
                                                #Resta la cantidad del inventario
                                                rest_cantidad(verify_name(namecompra,cantidadcompra, productos),cantidadcompra, productos)
                                                #Agrega el producto al carrito
                                                productos_carrito.append({'item_name':namecompra,'cantidad': cantidadcompra})
                                                #Agrega el producto a la LinkedList
                                                items_comprados.insert(namecompra, cont,items_comprados)
                                                #Agrega el pago
                                                pagos.append(total(namecompra,cantidadcompra, productos))
                                                cont = cont + 1
                            else:
                                console.print('Ingrese un numero positivo', style="error")


                if (opcioncompra == 2):
                    #Verifica si el carrito se encuentra vacío
                    if (cabeza == 0):
                        console.print('Su carrito se encuentra vacío', style="error")
                    else:
                        #Recorre la LinkedList de productos comprados
                        current = items_comprados.head
                        acu = 1
                        table_carrito = Table(title="CARRRITO")
                        table_carrito.add_column("No.", style="bold")
                        table_carrito.add_column("Producto", style="bold")
                        for i in range(cont):
                            table_carrito.add_row(str(acu), str(current.data))
                            console.print(table_carrito)
                            #print(acu, '. ', current.data)
                            acu = acu + 1
                            current = current.next
                        try:
                            numelim = int(input('Ingrese el numero del producto a eliminar del carrito \n'))
                        except:
                            console.print('Error', style="error")
                        else:
                            #Verifica si el numero a eliminar existe
                            if (numelim > acu - 1 or numelim < 1):
                                console.print('Ingrese un número valido', style="error")
                            else:
                                #Recorre la LinkedList del carrito
                                current = items_comprados.head
                                for i in range(cont):
                                    #Revisa si el valor se encuentra en el carrito
                                    if (search_carrito(current.data, productos_carrito) == 1):
                                        #Regresa la cantidad del producto
                                        saldar(current.data,search_cant(current.data, productos_carrito), productos)
                                        #Elimina el producto del carrito
                                        productos_carrito.pop(numelim - 1)
                                    current = current.next
                                #Elimina el producto de la LinkedList del carrito
                                items_comprados.delete(numelim)
                                cont = cont- 1
                                #Elimina el pago
                                pagos.pop(numelim - 1)
                                console.print('Producto eliminado exitosamente \n', style="success")


                if (opcioncompra == 3):
                    #Revisa si el carrito esta vacío
                    if cabeza == 0:
                        console.print('Carrito vacio', style="error")
                    else:
                        #Imprime la LinkedList del carrito
                        table_carrito = Table(title="CARRRITO")
                        table_carrito.add_column("No.", style="bold")
                        table_carrito.add_column("Producto", style="bold")
                        current = items_comprados.head
                        acu = 1
                            
                        for i in range(cont):
                            table_carrito.add_row(str(acu), str(current.data))
                        
                            acu = acu + 1
                            
                            #print(acu, '. ', current.data)
                            
                            current = current.next
                        #Imprime la cantidad de pagos a realizar
                        console.print(table_carrito)
                            
                        table_pagos = Table(title="")
                        table_pagos.add_column("Total a pagar", justify="center")
                        for x in pagos:
                            tot = tot + x
                        table_pagos.add_row(str(tot))
                        console.print(table_pagos)
                        # print('Total a pagar: ', tot, '\n')
                        tot = 0


                if (opcioncompra == 4):
                    #Revisa si el carrito esta vacío
                    if (cabeza == 0):
                        console.print('Carrito vacio', style="error")
                    else:
                        table_carrito = Table(title="CARRRITO")
                        table_carrito.add_column("No.", style="bold")
                        table_carrito.add_column("Producto", style="bold")
                        print('Productos en el carrito: \n')
                        #Imprime los elementos dentro del carrito
                        current = items_comprados.head
                        acu = 1
                        for i in range(cont):
                            table_carrito.add_row(str(acu), str(current.data))
                            console.print(table_carrito)
                            #print(acu, '. ', current.data)
                            acu = acu + 1
                            current = current.next
                        #Imprime los pagos a realizar
                        table_pagos = Table(title="")
                        table_pagos.add_column("Total pagado", justify="center")
                        for x in pagos:
                            tot = tot + x
                        table_pagos.add_row(str(tot))
                        console.print(table_pagos)
                        #print('Total a pagar: ', tot, '\n')
                        tot = 0
                        #Borra los elementos
                        pagos.clear()
                        productos_carrito.clear()
                        items_comprados.deleteAllNodes()
                        console.print('Gracias por su compra \n', style="success")
                        cabeza = 0
                        cont = 0


                if (opcioncompra > 5 or opcioncompra < 1):
                    console.print('Ingrese una opción valida', style="error")




        if opcion == 2:
            user = Prompt.ask("Ingrese su usuario \n")
            password = Prompt.ask("Ingrese su contraseña \n")
            #Validar la contraseña y usuario
            if user == usuario and password == contra:
                opcion1 = 0
                while (opcion1 != 8):
                    table_login = Table(title="INVENTARIO")
                    table_login.add_column("No.", style="bold")
                    table_login.add_column("Opcion", style="bold")

                    table_login.add_row("1.", "Añadir cantidad")
                    table_login.add_row("2.", "Remover cantidad")
                    table_login.add_row("3.", "Modificar productos")
                    table_login.add_row("4.", "Mostrar productos")
                    table_login.add_row("5.", "Añadir un item")
                    table_login.add_row("6.", "Eliminar un item")
                    table_login.add_row("7.", "Administrar productos vencidos")
                    table_login.add_row("8.", "Salir")

                    console.print(table_login)



                    
                   # print('\n')
                   # print('1. Añadir cantidad')
                   # print('2. Remover cantidad')
                   # print('3. Modificar productos')
                   # print('4. Mostrar productos')
                   # print('5. Añadir un item')
                   # print('6. Eliminar un item')
                   # print('7. Administrar productos vencidos')
                   # print('8. Salir')
                    try:
                        opcion1 = int(input('Ingrese la opcion a realizar: \n'))
                    except:
                        console.print('Error', style="error")
                    else:

                        if (opcion1 == 1):
                            try:
                                idpro = int(input('Ingrese el ID del producto: \n'))
                                cantsum = int(input('Ingrese la cantidad del producto que desea añadir: \n'))
                            except:
                                console.print('Error', style="error")
                            else:
                                #Verifica que la cantidad a sumar sea positiva
                                if (positivo(cantsum) == 1):                 
                                    #Suma la cantidad de productos
                                    if (sum_cantidad(idpro, cantsum, productos) == 0):
                                        console.print('Ingrese un numero valido', style="error")
                                    else:
                                        console.print('Cantidad actualizada con exito', style="success")

                                else:
                                    console.print('Ingrese una cantidad positiva', style="error")

                        if (opcion1 == 2):
                            try:
                                idpro = int(input('Ingrese el ID del producto: \n'))
                                cantrest = int(input('Ingrese la cantidad del producto que desea reducir: \n' ))
                            except:
                                console.print('Error', style="error")
                            else:
                                #Verifica que la cantidad a restar sea un numero positivo
                                if (positivo(cantrest) == 1):
                                    
                                    #Verifica que haya la cantidad suficiente de productos
                                    if (rest_cantidad(idpro, cantrest, productos) == 0):
                                        console.print( 'Error, no hay suficientes productos', style="error")
                                    else:
                                        console.print('Cantidad actualizada con exito', style="success" )
                                else:
                                    console.print('Ingrese un numero positivo', style="error")
                        if (opcion1 == 3):
                            opcion2 = 0
                            while (opcion2 != 5):
                                table_mod = Table(title="MENU")

                                table_mod.add_column("No.", style="bold")
                                table_mod.add_column("Opcion", style="bold")

                                table_mod.add_row("1.", "Modificar nombre")
                                table_mod.add_row("2.", "Modificar precio")
                                table_mod.add_row("3.", "Modificar cantidad")
                                table_mod.add_row("4.", "Modificar fecha de caducidad")
                                table_mod.add_row("5.", "Salir")

                                console.print(table_mod)

                                #print('1. Modificar nombre')
                                #print('2. Modificar precio')
                                #print('3. Modificar cantidad')
                                #print('4. Modificar fecha de caducidad')
                                #print('5. Salir')
                                try:
                                    opcion2 = int(input('Ingrese la opcion a realizar: \n'))
                                except:
                                    console.print('Error', style="error")
                                else:
                                    if (opcion2 == 1):
                                        try:
                                            idpro = int(input('Ingrese el ID del producto: \n'))
                                        except:
                                            console.print('Error', style="error")
                                        else:
                                            #Actualiza el nombre del producto
                                            namepro = (input('Ingrese el nuevo nombre del producto: \n'))
                                            if (edit_name(idpro, namepro, productos) == 1):
                                                console.print('Nombre actualizado con exito', style="success")
                                    if (opcion2 == 2):
                                        try:
                                            idpro = int(input('Ingrese el ID del producto: \n' ))
                                            preciopro = int(input('Ingrese el nuevo precio: \n'))
                                        except:
                                            console.print('Error', style="error")
                                        else:
                                            #Verifica que el precio sea positivo
                                            if (positivo(preciopro) == 1):
                                                #Edita el precio
                                                if (edit_precio(idpro, preciopro, productos) == 1):
                                                    console.print('Precio actualizado con exito', style="success")
                                            else:
                                                console.print('Ingrese un número positivo', style="error")
                                    if (opcion2 == 3):
                                        try:
                                            idpro = int(input('Ingrese el ID del producto: \n'))
                                            cantidadpro = int(input('Ingrese la nueva cantidad del producto: \n'))
                                        except:
                                            console.print('Error', style="error")
                                        else:
                                            #Verifica que la cantidad sea un numero positivo
                                            if (positivo(cantidadpro) == 1):
                                                #Edita la cantidad
                                                if (edit_cant(idpro, cantidadpro, productos) == 1):
                                                    console.print('Cantidad actualizada con exito', style="success")
                                            else:
                                                console.print('Ingrese un numero positivo', style="error")
                                    if(opcion2==4):
                                        try:
                                            idpro = int(input('Ingrese el ID del producto: \n'))
                                            fecha=datetime.strptime(input('Ingrese la fecha utilizando el formato dd-mm-aa: \n'), '%d-%m-%Y')
                                        except:
                                            console.print('Error', style="error")
                                        else:
                                            edit_fecha(idpro,fecha,productos)
                                    if (opcion2 < 1 or opcion2 > 5):
                                        console.print('Ingrese una opción valida', style="error")


                        table_base = Table(title='Productos disponibles')
                        table_base.add_column("item_id", style="bold")
                        table_base.add_column("item_name", style="bold")
                        table_base.add_column("precio", style="bold")
                        table_base.add_column("cantidad", style="bold")
                        table_base.add_column("caducidad", style="bold")                
                        if (opcion1 == 4):
                            #Imprime la base de datos
                                 for x in productos:
                                    table_base.add_row(str(x["item_id"]), x["item_name"], str(x["precio"]), str(x["cantidad"]), str(x["caducidad"]))
                                 console.print(table_base)

                        if (opcion1 == 5):
                            try:
                                id = int(input('Ingrese el ID del nuevo producto: \n'))
                                name = input('Ingrese el nombre del nuevo producto: \n')
                                price = int(input('Ingrese el precio del nuevo producto: \n'))
                                quantity = int(input('Ingrese la cantidad del nuevo producto: \n'))
                                vencimiento = datetime.strptime(input('Ingrese la fecha de caducidad utilizando el formato dd-mm-aa: \n'), '%d-%m-%Y')
                            except:
                                console.print('Error', style="error")
                            else:
                                #Verifica que la cantidad sea positiva al igual que el precio
                                if (positivo(quantity) == 1 and positivo(price) == 1):
                                    #Verifica que el ID no exista
                                    existente = verify_id(id, productos)
                                    if (existente == 0):
                                        console.print('ID ya existente', style="error")
                                    else:
                                        #Ingresa el nuevo producto
                                        productos.append({'item_id': id,'item_name': name,'precio': price,'cantidad': quantity, 'caducidad':vencimiento})
                                        actualizar()
                                        console.print('Producto ingresado con exito', style="success")
                                else:
                                    console.print('Ingrese número(s) positivo(s)', style="error")
                        if (opcion1 == 6):
                            try:
                                id = (int(input('Ingrese el ID del producto a eliminar: \n')))
                            except:
                                console.print('Error', style="error")
                            else:            
                                #Elimina el item
                                if (elim_item(id, productos) == 1):
                                    console.print('Item eliminado con exito', style="success")
                        if(opcion1==7):
                            flag=1
                            table_cad = Table(title="MENU")

                            table_cad.add_column("No.", style="bold")
                            table_cad.add_column("Opcion", style="bold")

                            table_cad.add_row("1.", "Mostrar productos vencidos")
                            table_cad.add_row("2.", "Eliminar productos vencidos")
                            table_cad.add_row("3.", "Eliminar producto más próximo a vencer")
                            table_cad.add_row("4.", "Salir")

                            console.print(table_cad)
                            
                            #print('1. Mostrar productos vencidos ')
                            #print('2. Eliminar productos vencidos')
                            #print('3. Eliminar producto más próximo a vencer')
                            #print('4. Salir')
                            while(flag==1):
                                try:
                                    opcionvencido=int(input('Ingrese la opción que desea realizar \n'))
                                except:
                                    console.print('Error', style="error")
                                else:
                                    productos1=productos.copy()
                                    sort(productos1)
                                    if(opcionvencido==1):
                                        if(vencidos(productos1)==0):
                                            console.print('No se encontraron productos vencidos', style="success")
                                    if(opcionvencido==2):
                                        if(elim_vencidos(productos1)==0):
                                            console.print('No se encontraron productos vencidos', style="success")
                                    if(opcionvencido==3):
                                        if(pop_item(productos1)==0):
                                            console.print('No se encontraron productos', style="error")
                                    if(opcionvencido==4):
                                        flag=0        
                        if (opcion1 < 1 and opcion1 > 7):
                            console.print('Ingrese una opcion valida', style="error")
            else:
                console.print("Usuario o contraseña incorrecta", style="error")

        if opcion != 1 and opcion != 2 and opcion != 3:
            console.print('Ingrese una opción valida', style="error")
