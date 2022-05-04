from LecturaArchivoTexto import actualizar
from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({"success": "green", "error": "bold red"})
console = Console(theme=custom_theme)

#Sumar a la cantidad de productos de un item
def sum_cantidad(id, cantidad, base_de_datos):

    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad no son enteros')
    else:
        for item in base_de_datos:
            if item['item_id'] == id:
                item['cantidad'] = int(item['cantidad']) + cantidad
                actualizar()
                return 1
        return 0


#Disminuir la cantidad de productos de un item
def rest_cantidad(id, cantidad, base_de_datos):

    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad no son enteros')
    else:
        for item in base_de_datos:
            if item['item_id'] == id:
                if (int(item['cantidad']) < cantidad):
                    return 0
                else:
                    item['cantidad'] = int(item['cantidad']) - cantidad
                    actualizar()
                    return 1
        return 0


#Modificar el nombre de producto
def edit_name(id, nombre, base_de_datos):
    if (type(id) not in [int]):
        raise TypeError('ID debe ser un entero')
    for item in base_de_datos:
        if item['item_id'] == id:
            item['item_name'] = nombre
            actualizar()
            return console.print('Nombre actualizado con exito', style="success")
    return console.print('Error, ID no encontrada', style="error")


#Modificar el precio de un producto
def edit_precio(id, precio, base_de_datos):
    if (type(id) not in [int] or type(precio) not in [int]):
        raise TypeError('ID o Precio deben ser enteros')
    for item in base_de_datos:
        if item['item_id'] == id:
            item['precio'] = precio
            actualizar()
            return 1
    return 0


#Modificar la cantidad de un producto
def edit_cant(id, cantidad, base_de_datos):
    if (type(id) not in [int] or type(cantidad) not in [int]):
        raise TypeError('ID o Cantidad deben ser enteros')
    for item in base_de_datos:
        if item['item_id'] == id:
            item['cantidad'] = cantidad
            actualizar()
            return 1
    return 0

#Edita la fecha de caducidad de un item
def edit_fecha(id,fecha,base_de_datos):
    for item in base_de_datos:
        if item['item_id']==id:
            item['caducidad']=fecha
            actualizar()
            return console.print('Fecha de caducidad actualizada con éxito', style="success")


#Eliminar un item
def elim_item(id, base_de_datos):
    if (type(id) not in [int]):
        raise TypeError('ID debe ser un entero')
    cont = 0
    for item in base_de_datos:
        if item['item_id'] == id:
            base_de_datos.pop(cont)
            actualizar()
            return 1
        cont = cont + 1
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
    for item in base_de_datos:
        if item['item_id'] == id:
            return 0
    return 1


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


#Retorna la cantidad al momento de eliminarse de la carrito
def saldar(nombre, cantidad, base_de_datos):
    if (type(cantidad) not in [int]):
        print('Error')
    for item in base_de_datos:
        if item['item_name'] == nombre:
            item['cantidad'] = item['cantidad'] + cantidad
            actualizar()


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

#Se utiliza para que no se pierda el archvio original de texto en el momento de usar el unittesting y profiling
def reparar(arr):
    from LecturaArchivoTexto import productos
    productos.clear()
    for item in arr:
        productos.append(item)
    actualizar()
    return 1
