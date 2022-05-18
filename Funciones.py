from BinarySearch import binarySearch, binarySearch_clientes
from Quicksort import sort_clientes
from LecturaArchivoTexto import actualizar
from rich.console import Console
from rich.theme import Theme
from datetime import datetime
custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

#Sumar a la cantidad de productos de un item
def sum_cantidad(id, cantidad, base_de_datos):

    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad no son enteros')
    else:
        try:
            item= binarySearch(base_de_datos, id)        
            item['cantidad'] = int(item['cantidad']) + cantidad
            actualizar(base_de_datos)
            return 1
        except:
            return 0

#Disminuir la cantidad de productos de un item
def rest_cantidad(id, cantidad, base_de_datos):

    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad no son enteros')
    else:
        try:
            item= binarySearch(base_de_datos,id)
            if (int(item['cantidad']) < cantidad):
                return 0
            else:
                item['cantidad'] = int(item['cantidad']) - cantidad
                actualizar(base_de_datos)
                return 1
        except:
            return 0


#Modificar el nombre de producto
def edit_name(id, nombre, base_de_datos):
    if (type(id) not in [int]):
        raise TypeError('ID debe ser un entero')
    try:
        item=binarySearch(base_de_datos,id)
        item['item_name'] = nombre
        actualizar(base_de_datos)
        return console.print('Nombre actualizado con exito', style="success")
    except:
        return console.print('Error, ID no encontrada', style="error")


#Modificar el precio de un producto
def edit_precio(id, precio, base_de_datos):
    if (type(id) not in [int] or type(precio) not in [int]):
        raise TypeError('ID o Precio deben ser enteros')
    try:
        item=binarySearch(base_de_datos,id)
        item['precio'] = precio
        actualizar(base_de_datos)
        return 1
    except:
        return 0


#Modificar la cantidad de un producto
def edit_cant(id, cantidad, base_de_datos):
    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad deben ser enteros')
    try:
        item=binarySearch(base_de_datos,id)
        item['cantidad'] = cantidad
        actualizar(base_de_datos)
        return 1
    except:
        return 0

#Edita la fecha de caducidad de un item
def edit_fecha(id,fecha,base_de_datos):
    try:
        item=binarySearch(base_de_datos,id)
        item['caducidad']=fecha
        actualizar(base_de_datos)
        return console.print('Fecha de caducidad actualizada con éxito', style="success")
    except:
        print('I no encontrado')


#Eliminar un item
def elim_item(id, base_de_datos):
    if (type(id) not in [int]):
        raise TypeError('ID debe ser un entero')
    try:
        item=binarySearch(base_de_datos,id)
        base_de_datos.remove(item)
        actualizar(base_de_datos)
        return 1
    except:
        return 0


#Verificar si existe el producto
def search_name(nombre, base_de_datos):
    for item in base_de_datos:
        if item['item_name'] == nombre:
            return 1
    return 0


#Verifica si el ID ya existe
def verify_id(id, base_de_datos):
    if (type(id) not in [int]):
        raise TypeError('Ingrese un entero')
    
    item=binarySearch(base_de_datos,id)
    if item is None:
        return 1
    else:
        return 0


#Verifica si existe suficiente cantidad del item
def verify_name(nombre, cantidad, base_de_datos):
    if (type(cantidad) not in [int]):
        raise TypeError('Cantidad debe ser un entero')
    for item in base_de_datos:
        if item['item_name'] == nombre:
            if item['cantidad'] >= cantidad:
                return item['item_id']
    return 0


#Total de la cantidad a pagar, precio * cantidad
def total(nombre, cantidad, base_de_datos):
    if (type(cantidad) not in [int]):
        raise TypeError('Cantidad debe ser un entero')
    for item in base_de_datos:
        if item['item_name'] == nombre:
            return cantidad * item['precio']


#Retorna la cantidad al momento de eliminarse del carrito
def saldar(nombre, cantidad, base_de_datos):
    if (type(cantidad) not in [int]):
        print('Error')
    for item in base_de_datos:
        if item['item_name'] == nombre:
            item['cantidad'] = item['cantidad'] + cantidad
            actualizar(base_de_datos)


#Valida si el item ya se encuentra en el carrito
def search_carrito(nombre, base_de_datos):
    for item in base_de_datos:
        if item['item_name'] == nombre:
            return 1
    return 0


#Cantidad de productos dentro de nuestro carrito
def search_cant(nombre, base_de_datos):
    for item in base_de_datos:
        if item['item_name'] == nombre:
            return item['cantidad']


#Validar que el numero ingresado sea un entero positivo
def positivo(num):
    if (type(num) not in [int]):
        raise TypeError('Debe ingresar un entero')
    if (num > 0):
        return 1
    else:
        return 0
#Busqueda de telefono a traves de binary search
def search_telefono(telefono, db):
    return binarySearch_clientes(db,telefono)

#Calcula la diferencia de días entre la fecha de caducidad y hoy
def days_between(d2):
    d1 = datetime.today()
    d2 = datetime.strptime(d2, '%Y-%m-%d %H:%M:%S')
    return (d2 - d1).days+1

#Ingresa los clientes a la base de datos
def ingresar_cliente(nombre, direccion, telefono, tarjeta,db):
    db.append({'nombre':nombre, 'direccion':direccion,'numero':telefono, 'tarjeta':tarjeta})
    sort_clientes(db)
    item = {'nombre':nombre, 'direccion':direccion,'numero':telefono, 'tarjeta':tarjeta}
    return item
    
    
